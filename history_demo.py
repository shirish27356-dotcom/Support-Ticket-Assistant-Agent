from langchain.messages import SystemMessage, HumanMessage
from langchain_groq import ChatGroq
import os
from dotenv import load_dotenv

load_dotenv()



model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0,max_retries=2,
                   timeout=1
                   )

history = [
    SystemMessage(content="You are a helpful python assistant.")]

def ask(question):
    history.append(HumanMessage(content=question))
    response = model.invoke(history)
    history.append(response)
    return response.text

print(ask("My fav language is python."))

print(ask("which language which i mention."))

