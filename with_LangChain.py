import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq


load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0)

rsponse = model.invoke("Explain the LLM in one line")

print(rsponse.text)



