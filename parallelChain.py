import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel



load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY is not set in the environment")

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0,max_retries=2,
                   timeout=10.0)


summary=ChatPromptTemplate.from_template(
    "Summarize the following {topic} in one line") | model | StrOutputParser()


key_points = ChatPromptTemplate.from_template(
    "List 3 key points about {topic} in bullet points") | model | StrOutputParser()

parallel_chain = RunnableParallel(
    summary = summary,
    key_points = key_points)

result = parallel_chain.invoke({"topic": "Langchain"})

print(result["summary"])
print(result["key_points"])
