import streamlit as st 
import os
from rag_engine import build_vectorstore, ask_question

# -----------------------------
# PAGE CONFIG
# -----------------------------
st.set_page_config(page_title="AI PDF RAG", layout="centered")

st.title("📄 AI Document Q&A (PDF + TXT RAG)")
st.markdown("Upload a PDF or TXT file and chat with it.")

# -----------------------------
# SESSION STATE
# -----------------------------
if "vectorstore" not in st.session_state:
    st.session_state.vectorstore = None

if "chat" not in st.session_state:
    st.session_state.chat = []


# -----------------------------
# FILE UPLOAD (PDF + TXT)
# -----------------------------
uploaded_file = st.file_uploader(
    "Upload your document",
    type=["pdf", "txt"]
)

if uploaded_file:

    os.makedirs("temp", exist_ok=True)

    file_path = f"temp/{uploaded_file.name}"

    with open(file_path, "wb") as f:
        f.write(uploaded_file.getbuffer())

    st.session_state.vectorstore = build_vectorstore(file_path)

    st.success("Document processed successfully!")


# -----------------------------
# CHAT INPUT
# -----------------------------
query = st.chat_input("Ask something about your document...")

if query and st.session_state.vectorstore:

    answer = ask_question(st.session_state.vectorstore, query)

    st.session_state.chat.append(("user", query))
    st.session_state.chat.append(("bot", answer))


# -----------------------------
# CHAT DISPLAY
# -----------------------------
for role, msg in st.session_state.chat:

    if role == "user":
        st.markdown(
            f"<div style='text-align:right; background:#DCF8C6; padding:10px; border-radius:10px; margin:5px'>{msg}</div>",
            unsafe_allow_html=True
        )
    else:
        st.markdown(
            f"<div style='text-align:left; background:#F1F0F0; padding:10px; border-radius:10px; margin:5px'>{msg}</div>",
            unsafe_allow_html=True
        )