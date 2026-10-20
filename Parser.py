from langchain_core.output_parsers import StrOutputParser

parser = StrOutputParser()

result = parser.invoke("This is a test string.")

print(result)
print(type(result))
