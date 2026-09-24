from pathlib import Path
import sys

sys.path.insert(0, str(Path(__file__).resolve().parents[1]))

from app import extract_graph_facts


def test_extract_graph_facts_identifies_entities_and_relations():
    text = """
    The system uses FastAPI and ChromaDB. FastAPI connects to OpenAI GPT-4.
    The user uploads a PDF through the API.
    """
    facts = extract_graph_facts(text)
    assert any(f["source"] == "FastAPI" for f in facts)
    assert any(f["relation"] == "uses" for f in facts)
    assert any(f["target"] == "OpenAI GPT-4" for f in facts)
