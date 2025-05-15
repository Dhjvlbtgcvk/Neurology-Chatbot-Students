# 🧠 Neurology Chatbot Project

A conversational AI chatbot designed to answer neurology-related questions based on the textbook **"Clinical Neurology" by David Greenberg**. This chatbot utilizes **LangChain**, **Groq's LLaMA-3 LLM**, **FAISS** for vector search, and **HuggingFace embeddings**.

---

## 🚀 Features

- Chat with a Neurology-focused AI
- Based on "Clinical Neurology" by David Greenberg (PDF)
- Natural language question answering using LLaMA-3
- PDF loader and text chunking for semantic search
- Streamlit-based user interface
- Powered by LangChain + FAISS + HuggingFace + Groq

---

## 🗃️ Dataset

- **Source**: *Clinical Neurology* by David Greenberg  
- **Format**: PDF (~500 pages)  
- **Chunks**: 2000 characters each with 20-character overlap  
- **Usage**: Converted into vector embeddings using `sentence-transformers/all-MiniLM-L6-v2` and stored in FAISS

---

## 🧑‍💻 Project Structure

```plaintext
Neurology-Chatbot-Students/
│
├── research/
│   └── test.py                # Main backend chatbot logic
├── streamlit_app.py           # Streamlit chatbot UI
├── requirements.txt           # Python dependencies
├── .env                       # Environment variables (API keys)
├── README.md                  # Project documentation
├── Clinical_Neurology.pdf     # Source textbook
└── vectorstore/               # Saved FAISS index (optional)

How to Use it:

1. Clone the Repository
git clone https://github.com/yourusername/neurology-chatbot.git
cd neurology-chatbot

2. Create and Activate Virtual Environment
python -m venv myvenv
source myvenv/bin/activate      # On Windows: myvenv\Scripts\activate

3. Install Dependencies
pip install -r requirements.txt

Add API Keys in (.env)
GROQ_API_KEY=your_groq_key
HUGGINGFACEHUB_API_KEY=your_hf_key


