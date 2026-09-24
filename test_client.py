"""
Simple test client for RAG System API
Run this after starting the server with setup_and_run.bat
"""
import requests
import json
import os
from pathlib import Path

BASE_URL = "http://localhost:8000"

def test_root():
    """Test the root endpoint"""
    print("\n" + "="*50)
    print("Testing Root Endpoint...")
    print("="*50)
    try:
        response = requests.get(f"{BASE_URL}/")
        print(f"Status Code: {response.status_code}")
        print(f"Response: {response.json()}")
        return True
    except Exception as e:
        print(f"❌ Error: {e}")
        print("Make sure the server is running!")
        return False

def ingest_document(file_path):
    """Upload and ingest a document"""
    print("\n" + "="*50)
    print("Testing Document Ingestion...")
    print("="*50)
    
    if not os.path.exists(file_path):
        print(f"❌ File not found: {file_path}")
        return False
    
    try:
        with open(file_path, "rb") as f:
            files = {"file": (os.path.basename(file_path), f)}
            response = requests.post(f"{BASE_URL}/api/v1/ingest", files=files)
            print(f"Status Code: {response.status_code}")
            print(f"Response: {response.json()}")
            return response.status_code == 200
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def query_system(query_text, session_id="test_session"):
    """Query the RAG system"""
    print("\n" + "="*50)
    print("Testing Query Endpoint...")
    print("="*50)
    print(f"Query: {query_text}")
    
    try:
        query_data = {
            "query": query_text,
            "session_id": session_id
        }
        response = requests.post(
            f"{BASE_URL}/api/v1/query",
            json=query_data,
            headers={"Content-Type": "application/json"}
        )
        print(f"Status Code: {response.status_code}")
        
        if response.status_code == 200:
            result = response.json()
            print(f"\n📝 Answer: {result['answer']}")
            print(f"\n📚 Sources ({len(result['sources'])} found):")
            for i, source in enumerate(result['sources'], 1):
                print(f"  {i}. {source}")
            return True
        else:
            print(f"Response: {response.text}")
            return False
    except Exception as e:
        print(f"❌ Error: {e}")
        return False

def main():
    print("\n")
    print("╔═══════════════════════════════════════════════════╗")
    print("║       RAG System - API Test Client               ║")
    print("╚═══════════════════════════════════════════════════╝")
    
    # Test 1: Root endpoint
    if not test_root():
        print("\n❌ Server is not running!")
        print("Please start the server first using setup_and_run.bat")
        return
    
    print("\n✅ Server is running!")
    
    # Interactive menu
    while True:
        print("\n" + "="*50)
        print("Choose an option:")
        print("="*50)
        print("1. Ingest a document")
        print("2. Query the system")
        print("3. Run full test (ingest + query)")
        print("4. Exit")
        print("="*50)
        
        choice = input("\nEnter your choice (1-4): ").strip()
        
        if choice == "1":
            file_path = input("Enter full path to your document: ").strip()
            file_path = file_path.strip('"')  # Remove quotes if any
            ingest_document(file_path)
            
        elif choice == "2":
            query = input("Enter your question: ").strip()
            if query:
                query_system(query)
            else:
                print("❌ Query cannot be empty!")
                
        elif choice == "3":
            print("\nRunning full test...")
            file_path = input("Enter full path to your document: ").strip()
            file_path = file_path.strip('"')
            
            if ingest_document(file_path):
                print("\n⏳ Waiting for ingestion to complete...")
                import time
                time.sleep(2)
                
                query = input("\nEnter your question about the document: ").strip()
                if query:
                    query_system(query)
                    
        elif choice == "4":
            print("\n👋 Goodbye!")
            break
            
        else:
            print("❌ Invalid choice!")

if __name__ == "__main__":
    try:
        main()
    except KeyboardInterrupt:
        print("\n\n👋 Interrupted by user. Goodbye!")
    except Exception as e:
        print(f"\n❌ Unexpected error: {e}")
