from langchain_community.document_loaders import TextLoader, PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_huggingface import HuggingFaceEmbeddings
from langchain_community.vectorstores import FAISS
from langchain_groq import ChatGroq
from dotenv import load_dotenv

load_dotenv()


# -----------------------------
# 1. LOAD DOCUMENT (TXT OR PDF)
# -----------------------------
def load_document(file_path):
    if file_path.endswith(".pdf"):
        loader = PyPDFLoader(file_path)
    else:
        loader = TextLoader(file_path)

    return loader.load()


# -----------------------------
# 2. BUILD VECTOR STORE
# -----------------------------
def build_vectorstore(file_path):

    documents = load_document(file_path)

    splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=50
    )

    docs = splitter.split_documents(documents)

    embedding = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    vectorstore = FAISS.from_documents(docs, embedding)

    return vectorstore


# -----------------------------
# 3. ASK QUESTION (RAG PIPELINE)
# -----------------------------
def ask_question(vectorstore, query):

    retriever = vectorstore.as_retriever()
    retrieved_docs = retriever.invoke(query)

    context = "\n".join([doc.page_content for doc in retrieved_docs])

    llm = ChatGroq(model="llama-3.3-70b-versatile")

    prompt = f"""
You are a helpful assistant.

Context:
{context}

Question:
{query}
"""

    response = llm.invoke(prompt)

    return response.content