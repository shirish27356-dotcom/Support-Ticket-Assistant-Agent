from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("user", "Explain the {topic} in simple language")
])

result = prompt.invoke({"topic": "Python programming"})

print(result.to_string())
