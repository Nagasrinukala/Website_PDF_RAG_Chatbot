# **Website_PDF_RAG_Chatbot**

A Retrieval-Augmented Generation (RAG) chatbot that can answer questions from website URLs and PDF documents using embeddings and LLM.

# **Project UI**
<img width="1353" height="561" alt="image" src="https://github.com/user-attachments/assets/27a6773b-7c3b-4dd3-bf16-8cfd0b5e3b67" />

## **Problem Statement**
Many chatbots only answer general knowledge questions. They cannot answer questions from specific websites or documents.
This project solves that problem by building a RAG-based chatbot that can read website content and PDF documents and answer user questions based on that data.

# **Upload files**
Website_RAG_Chatbot/
│
├── assets/
│   └── background.jpg
│
├── website_chatbot/
│   ├── __init__.py
│   ├── chatbot.py
│   ├── config.py
│   ├── pdf_reader.py
│   ├── rag.py
│   ├── scraper.py
│   └── vector_store.py
│
├── .gitattributes
├── README.md
├── app.py
├── requirements.txt

## **Workflow:**
The project uses a Retrieval-Augmented Generation (RAG) architecture where documents are converted into embeddings and stored in a vector database. When a user asks a question, relevant content is retrieved and passed to the LLM to generate an accurate answer.

1.User enters Website URLs
2.User uploads PDF
3.System scrapes website content
4.System reads PDF text
5.Text is converted into chunks
6.Embeddings are created
7.Stored in Vector Database
8.User asks question
9.Relevant chunks retrieved
10.LLM generates answer

## **Technologies Used**
**Programming & Frameworks**
1.Python
2.Gradio – User Interface
3.Hugging Face Spaces – Deployment
**RAG Pipeline Components**
4.LangChain – RAG pipeline orchestration
5.FAISS – Vector Database
6.Sentence Transformers – Text Embeddings
7.BeautifulSoup – Web Scraping
8.PyPDF – PDF Text Extraction
**LLM & API**
9.Groq – LLM Inference API
10.Open Source LLM (LLaMA / Mixtral via Groq)


