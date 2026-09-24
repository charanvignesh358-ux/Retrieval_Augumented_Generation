from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder, PromptTemplate
from langchain_core.runnables.history import RunnableWithMessageHistory
from langchain_core.chat_history import BaseChatMessageHistory, InMemoryChatMessageHistory

try:  # langchain 0.x
    from langchain.chains import create_history_aware_retriever, create_retrieval_chain
    from langchain.chains.combine_documents import create_stuff_documents_chain
except ImportError:  # langchain 1.x moved these to langchain-classic
    from langchain_classic.chains import create_history_aware_retriever, create_retrieval_chain
    from langchain_classic.chains.combine_documents import create_stuff_documents_chain

from app.db.vector_store import VectorStore
from app.core.config import settings

# Simple in-memory history (one per user + session)
store = {}


def get_session_history(session_id: str) -> BaseChatMessageHistory:
    if session_id not in store:
        store[session_id] = InMemoryChatMessageHistory()
    return store[session_id]


class RAGChain:
    def __init__(self, vector_store: VectorStore = None):
        if not settings.GROQ_API_KEY:
            raise ValueError("GROQ_API_KEY is missing. Add it to RAG\\.env (free key: https://console.groq.com/keys)")

        self.vector_store = vector_store or VectorStore()
        self.llm = ChatGroq(
            model=settings.GROQ_MODEL,
            temperature=0,
            api_key=settings.GROQ_API_KEY,
        )

        contextualize_q_system_prompt = (
            "Given a chat history and the latest user question which might reference context in the "
            "chat history, formulate a standalone question which can be understood without the chat "
            "history. Do NOT answer the question, just reformulate it if needed and otherwise return it as is."
        )
        self.contextualize_q_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", contextualize_q_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )

        qa_system_prompt = (
            "You are an enterprise document assistant. Answer ONLY using the context below. "
            "Cite the source inline like [file, page N]. If the answer is not in the context, reply exactly: "
            "\"I don't know based on the available documents.\" Never invent facts. Keep answers concise.\n\n"
            "{context}"
        )
        self.qa_prompt = ChatPromptTemplate.from_messages(
            [
                ("system", qa_system_prompt),
                MessagesPlaceholder("chat_history"),
                ("human", "{input}"),
            ]
        )
        self._chain = None

    def get_chain(self):
        """Builds (once) the RAG chain with memory."""
        if self._chain is not None:
            return self._chain

        retriever = self.vector_store.as_retriever()
        history_aware_retriever = create_history_aware_retriever(
            self.llm, retriever, self.contextualize_q_prompt
        )
        # Put the file name + page in front of each chunk so the model can cite it
        doc_prompt = PromptTemplate.from_template("[Source: {source}, page {page}]\n{page_content}")
        question_answer_chain = create_stuff_documents_chain(
            self.llm, self.qa_prompt, document_prompt=doc_prompt
        )
        rag_chain = create_retrieval_chain(history_aware_retriever, question_answer_chain)

        self._chain = RunnableWithMessageHistory(
            rag_chain,
            get_session_history,
            input_messages_key="input",
            history_messages_key="chat_history",
            output_messages_key="answer",
        )
        return self._chain

    def run(self, query: str, session_id: str = "default_session"):
        response = self.get_chain().invoke(
            {"input": query},
            config={"configurable": {"session_id": session_id}},
        )
        return {
            "answer": response["answer"],
            "source_documents": [
                {**doc.metadata, "excerpt": doc.page_content[:300]} for doc in response["context"]
            ],
        }
