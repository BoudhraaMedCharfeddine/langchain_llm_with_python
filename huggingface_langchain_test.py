from langchain.prompts import PromptTemplate
from langchain_huggingface import HuggingFaceEndpoint


question = "Qui a remporté la Coupe du Monde de la FIFA en 2018 ? "

template = """Question : {question}

Réponse : Réfléchissons étape par étape."""

prompt = PromptTemplate.from_template(template)


repo_id="mistralai/Mixtral-8x7B-Instruct-v0.1"


llm = HuggingFaceEndpoint(
    repo_id=repo_id,
    temperature=0.2
)
llm_chain = prompt | llm
print(llm_chain.invoke({"question": question}))