from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from langchain_groq import ChatGroq
from langchain_community.embeddings import HuggingFaceEmbeddings
from dotenv import load_dotenv
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain.chains import RetrievalQA
import os


load_dotenv()
GROQ_KEY = os.getenv("GROQ_API_KEY")
HF_KEY = os.getenv("HUGGINGFACEHUB_API_KEY")

Path_file = r"C:\Users\M.Hasnain Asif\Neurology-Chatbot-Students\Clinical Neurology 9 Edition (www.myuptodate.com).pdf"


loader = PyPDFLoader(file_path=Path_file)
documents = loader.load()


text_splitter = RecursiveCharacterTextSplitter(chunk_size=2000, chunk_overlap=20)
chunks_documents = text_splitter.split_documents(documents)


embedding_model = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")


vectorstore = FAISS.from_documents(chunks_documents, embedding_model)


retriever = vectorstore.as_retriever()


groq_model = ChatGroq(
    model="llama3-70b-8192",
    api_key=GROQ_KEY,
    temperature=0.7
)

PARSER = StrOutputParser()


qa_chain = RetrievalQA.from_chain_type(
    llm=groq_model,
    retriever=retriever,
    return_source_documents=True
    
)


query = input("Enter your query: ")


result = qa_chain.invoke(query)


print(result)
