from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.document_loaders import PyPDFLoader
from langchain_ollama import OllamaEmbeddings
from langchain_ollama import ChatOllama
from langchain_community.vectorstores import FAISS


def load_and_split_documents():
    file_paths = [
        "data/bgita.pdf",
        "data/Bhagavad-gita-As-It-Is.pdf",
        "data/The Bhagavad Gita.pdf"
    ]

    docs = []
    for file_path in file_paths:
        if file_path.endswith(".pdf"):
            loader = PyPDFLoader(file_path)
            docs.extend(loader.load())
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=50,
        add_start_index=True,
    )
    split_docs = text_splitter.split_documents(docs)
    return split_docs


def create_vector_store(documents, model_name="llama2"):
    embeddings = OllamaEmbeddings(model=model_name)
    vector_store = FAISS.from_documents(documents, embeddings)
    return vector_store
