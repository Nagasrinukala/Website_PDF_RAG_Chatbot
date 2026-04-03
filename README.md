# **Website_PDF_RAG_Chatbot**

A Retrieval-Augmented Generation (RAG) chatbot that can answer questions from website URLs and PDF documents using embeddings and LLM.

## Live Demo
HuggingFace Space:
https://huggingface.co/spaces/Nagasrinukala/Website_RAG_Chatbot

# **Project UI**
<img width="1353" height="561" alt="image" src="https://github.com/user-attachments/assets/27a6773b-7c3b-4dd3-bf16-8cfd0b5e3b67" />

## **Problem Statement**
Many chatbots only answer general knowledge questions. They cannot answer questions from specific websites or documents.
This project solves that problem by building a RAG-based chatbot that can read website content and PDF documents and answer user questions based on that data.

# **Upload files**
<img width="660" height="345" alt="image" src="https://github.com/user-attachments/assets/56bc1b16-e6d9-4f54-891f-3b2edd877dc3" />

### **Explain each file**
<img width="675" height="284" alt="image" src="https://github.com/user-attachments/assets/088fa578-0194-4d88-a52a-16dda57d28af" />
<img width="700" height="368" alt="image" src="https://github.com/user-attachments/assets/f4418407-2b92-49e5-aa9d-603928de738b" />



## **Workflow:**
The project uses a Retrieval-Augmented Generation (RAG) architecture where documents are converted into embeddings and stored in a vector database. When a user asks a question, relevant content is retrieved and passed to the LLM to generate an accurate answer.

<img width="642" height="269" alt="image" src="https://github.com/user-attachments/assets/1cdb43e1-d1a0-4cff-a6bb-d2b904d7dab9" />

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


## Usage

1. Enter website URLs (comma separated) in the input box.
2. Upload a PDF document.
3. Click **Load Data** to process website and PDF content.
4. Ask questions in the chatbot input box.
5. The chatbot will answer based on the website and PDF content using RAG.

### Example Questions
- Summarize the website content
- What is explained in the PDF?
- Give key points from the document
- Explain the main topic

## Future Improvements

- Support multiple PDF uploads
- Add chat history memory
- Add document source citations
- Improve UI design
- Use more advanced LLM models
- Add user authentication
- Deploy using Docker
- Add streaming responses
- Add database storage for documents


