""" from langchain_community.tools import TavilySearchResults
from langchain_core.messages import HumanMessage

tool = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True
)

tools = [tool]

from langchain_mistralai import ChatMistralAI

model = ChatMistralAI(model="mistral-large-latest")


response = model.invoke([HumanMessage(content="salut !")])
print(response.content) """



from langchain_mistralai import ChatMistralAI
from langchain_core.prompts import ChatPromptTemplate 
from langchain_core.messages import HumanMessage

from langchain_community.tools import TavilySearchResults

tool = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True
)

tools = [tool]

mistral_model = "mistral-large-latest"
llm = ChatMistralAI(model=mistral_model, temperature=0)

#response = llm.invoke([HumanMessage(content="salut !")])

model_with_tools = llm.bind_tools(tools)

"""print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}") """

response = model_with_tools.invoke([HumanMessage(content="Quel temps fait-il à Lisbonne ?")])

print(f"ContentString: {response.content}")
print(f"ToolCalls: {response.tool_calls}")

