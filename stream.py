from langchain_groq import ChatGroq

from dotenv import load_dotenv

load_dotenv()

model = ChatGroq(model="openai/gpt-oss-20b", temperature=0.0,max_retries=2,
                   timeout=10.0)

for chunk in model.stream("Explain the Langchain in one line. Give 3 examples."):
    print(chunk.content, end="", flush=True)


print()

