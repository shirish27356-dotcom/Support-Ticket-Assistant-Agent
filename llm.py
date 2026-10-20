import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

def get_model():
    if not os.getenv("GROQ_API_KEY"):
        raise ValueError("GROQ_API_KEY is not set in the environment variables.")

    return ChatGroq(model="openai/gpt-oss-20b", temperature=0.0,max_retries=2,
                       timeout=10.0)

