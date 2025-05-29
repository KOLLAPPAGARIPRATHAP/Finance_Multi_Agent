from langchain.embeddings import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
import os

# For demo: use dummy embeddings; replace with your own or MCP embeddings
# Make sure to install faiss-cpu: pip install faiss-cpu

def build_faiss_index(texts):
    """
    Build FAISS index from list of texts.
    """
    try:
        # Use OpenAI embeddings as a placeholder, replace with your embeddings provider
        embedding_model = OpenAIEmbeddings()
        text_splitter = RecursiveCharacterTextSplitter(chunk_size=500, chunk_overlap=50)
        docs = []
        for text in texts:
            splits = text_splitter.split_text(text)
            for chunk in splits:
                docs.append(Document(page_content=chunk))

        index = FAISS.from_documents(docs, embedding_model)
        return index
    except Exception as e:
        print(f"Retriever Agent error: {e}")
        return None

def retrieve_top_k(index, query, k=3):
    """
    Retrieve top-k documents relevant to the query.
    """
    try:
        results = index.similarity_search(query, k=k)
        return results
    except Exception as e:
        print(f"Retriever Agent retrieval error: {e}")
        return []

if __name__ == "__main__":
    sample_texts = [
        "TSMC beat earnings estimates by 4 percent this quarter.",
        "Samsung missed earnings estimates by 2 percent.",
        "Asia tech sector shows neutral sentiment today."
    ]
    index = build_faiss_index(sample_texts)
    if index:
        results = retrieve_top_k(index, "earnings surprises", 2)
        for r in results:
            print(r.page_content)
