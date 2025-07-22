from langchain_community.tools import TavilySearchResults
import json

tool = TavilySearchResults(
    max_results=5,
    search_depth="advanced",
    include_answer=True,
    include_raw_content=True,
    include_images=True
)

#res = tool.invoke({"query": "Que s'est-il passé au dernier tournoi de tennis de Roland Garros ?"})

#print(res)

model_generated_tool_call = {
    "args": {"query": "pays hôte de l'euro 2024"},
    "id": "1",
    "name": "tavily",
    "type": "tool_call",
}

tool_msg = tool.invoke(model_generated_tool_call)

#print(tool_msg.content[:400])

# Abréger les résultats à des fins de démonstration
print(json.dumps({k: str(v)[:200] for k, v in tool_msg.artifact.items()}, indent=2))