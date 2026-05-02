# 📄 AI Document Q&A (RAG System with Groq + FAISS)

An AI-powered Retrieval-Augmented Generation (RAG) application that allows users to upload **PDF or TXT documents** and ask questions about their content using **LangChain, FAISS, HuggingFace Embeddings, and Groq LLM**, all wrapped in a clean **Streamlit UI**.

---

## 🚀 Features

- 📁 Upload PDF or TXT documents
- 🧠 RAG-based question answering system
- 🔍 Semantic search using FAISS vector database
- 🤖 Fast LLM responses using Groq (LLaMA 3)
- 💬 Chat-style interactive UI with Streamlit
- ⚡ Lightweight embeddings using Sentence Transformers

---

## 🏗️ Project Architecture
User Upload (PDF/TXT)

↓

Document Loader (LangChain)

↓

Text Splitter (Chunking)

↓

Embeddings (HuggingFace)

↓

FAISS Vector Store

↓

Retriever (Semantic Search)

↓

Groq LLM (LLaMA 3)

↓

Final Answer

↓

Streamlit UI Response


---
## 🔑 Environment Variables

`Create a .env file in the root directory:`
GROQ_API_KEY=your_groq_api_key_here
HUGGINGFACEHUB_API_TOKEN=your_huggingface_api_here
