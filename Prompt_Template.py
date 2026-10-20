from langchain_core.prompts import PromptTemplate

prompt = PromptTemplate.from_template("Explain the {topic} in simple language")

result = prompt.invoke({"topic": "Python programming"})

print(result.to_string())

