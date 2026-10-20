from langchain.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()



model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0,max_retries=2,
                   timeout=10.0)

messages = [
    SystemMessage(content="You are a helpful python assistant."),
    HumanMessage(content="Explain use of python dictionary with examples.")
    ,]

response = model.invoke(messages)

print(response.text)

