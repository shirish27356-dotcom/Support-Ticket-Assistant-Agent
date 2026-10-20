from dotenv import load_dotenv
from langchain_groq import ChatGroq

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0,
                 max_retries=2)

questions= [
    "Explain the Langchain in one line. .",
    "Explain RAG in simple words",
    "Explain Agentic AI in simple words."
    ]


responses = model.batch(questions)

for question, response in zip(questions, responses):
    print(f"Question: {question}")
    print(f"Response: {response.text}\n")
    