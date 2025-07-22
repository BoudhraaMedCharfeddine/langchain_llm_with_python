from langchain_core.prompts import ChatPromptTemplate

prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "tu es un assistant utile qui traduit de {input_language} à {output_language}.",
        ),
        ("human", "{input}"),
    ]
)

from langchain_mistralai import ChatMistralAI

llm = ChatMistralAI(
    model="mistral-large-latest",
    temperature=0
)

chain = prompt | llm
print(chain.invoke(
    {
        "input_language": "Anglais",
        "output_language": "Français",
        "input": "I love coding.",
    }
))