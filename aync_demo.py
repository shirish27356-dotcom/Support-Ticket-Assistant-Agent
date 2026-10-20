import asyncio
from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0,
                 max_retries=2)

async def main():
    questions = [
        "Explain the Langchain in one line.",
        "Explain RAG in simple words",
        "Explain Agentic AI in simple words."
    ]
    response = await asyncio.gather(*[model.ainvoke(question) for question in questions])
   
   
    for question, res in zip(questions, response):
        print(f"Question: {question}")
        print(f"Response: {res.text}\n")

asyncio.run(main())
