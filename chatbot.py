from openai import OpenAI
import os
from dotenv import load_dotenv
from .rag import split_text
from .vector_store import create_vector_store, search_vector_store

load_dotenv()

client = OpenAI(
    api_key=os.getenv("API_KEY"),
    base_url="https://api.groq.com/openai/v1"
)

vector_created = False

def reset_vector_store():
    global vector_created
    vector_created = False

def ask_chatbot(context, question, chat_history):
    global vector_created

    # Create vector DB only once
    if not vector_created and context.strip() != "":
        chunks = split_text(context)
        print("Chunks created:", len(chunks))
        create_vector_store(chunks)
        vector_created = True

    relevant_context = search_vector_store(question)

    if relevant_context.strip() == "":
        return "I cannot find the answer on this website."

    prompt = f"""
You are a website assistant chatbot.

Rules:
- Answer only from the provided content
- If answer not found, say:
  "I cannot find the answer on this website."

Website Content:
{relevant_context}

Chat History:
{chat_history}

Question:
{question}

Answer:
"""

    response = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": prompt}],
        temperature=0.3,
        max_tokens=500
    )

    return response.choices[0].message.content