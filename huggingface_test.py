
from langchain_huggingface import HuggingFaceEndpoint

repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1"

llm = HuggingFaceEndpoint(
    repo_id=repo_id
)

text = "Traduire du français à l'anglais : 'Je m'appelle Rod'"
print(llm.invoke(text))