import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.output_parsers import StrOutputParser
from langchain_groq import ChatGroq
from langchain_core.runnables import RunnableParallel
from langchain_core.messages import HumanMessage, SystemMessage, AIMessage

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0,max_retries=2,
                   timeout=10.0)

prompt = ChatPromptTemplate.from_messages([
("system", "You are {persona}. Answer in simple English."),
MessagesPlaceholder("history"),
("human", "{question}"),
])

chat_chain = prompt | model | StrOutputParser()

history = []

question = "My name is Shirish"
answer = chat_chain.invoke({"persona": "a helpful assistant", "history": history, "question": question})
history.extend([HumanMessage(content=question), AIMessage(content=answer)])

question = "What is my name"
answer = chat_chain.invoke({"persona": "a helpful assistant", "history": history, "question": question})
history.extend([HumanMessage(content=question), AIMessage(content=answer)])

print(answer)


