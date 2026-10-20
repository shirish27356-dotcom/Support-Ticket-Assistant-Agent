import os
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser


load_dotenv()

if not os.getenv("GROQ_API_KEY"):
    raise ValueError("GROQ_API_KEY is not set in the environment")

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0,max_retries=2,
                   timeout=10.0)

summary_prompt = ChatPromptTemplate.from_template(
    "Summarize the following {topic} in one line"
)

summary_chain = summary_prompt | model | StrOutputParser()

print(summary_chain.invoke({"topic": "Langchain"}))





