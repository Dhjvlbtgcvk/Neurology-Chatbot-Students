import streamlit as st
from dotenv import load_dotenv
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os


load_dotenv()
GROQ_KEY = os.getenv("GROQ_API_KEY")


st.set_page_config(page_title="Neurology PDF Chatbot", layout="centered")
st.title("🧠 Neurology PDF Chatbot")


Path_file = r"C:\Users\M.Hasnain Asif\Neurology-Chatbot-Students\Clinical Neurology 9 Edition (www.myuptodate.com).pdf"


@st.cache_resource
def load_retriever():
    loader = PyPDFLoader(file_path=Path_file)
    documents = loader.load()
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=20)
    chunks_documents = text_splitter.split_documents(documents)

    embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
    vectorstore = FAISS.from_documents(chunks_documents, embedding_model)

    return vectorstore.as_retriever()

retriever = load_retriever()


groq_model = ChatGroq(
    model="llama3-70b-8192",
    api_key=GROQ_KEY,
    temperature=0.7
)

qa_chain = RetrievalQA.from_chain_type(
    llm=groq_model,
    retriever=retriever,
    return_source_documents=False
)


user_input = st.text_input("Ask something about the PDF:", placeholder="Type your question...")

if st.button("Get Answer") and user_input:
    with st.spinner("Thinking..."):
        result = qa_chain.invoke(user_input)
        st.success("Here's the answer:")
        st.write(result["result"])
