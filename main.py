from langchain_ollama import OllamaLLM

model = OllamaLLM(model="deepseek-r1")

result = model.invoke(input="Hello World")
print(result)
