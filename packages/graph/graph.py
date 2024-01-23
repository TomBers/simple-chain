from langchain_community.tools.tavily_search import TavilySearchResults
from langgraph.prebuilt import ToolExecutor
from langchain_openai import ChatOpenAI
from langchain.tools.render import format_tool_to_openai_function


from langchain_core.messages import HumanMessage

from state_graph import app

from dotenv import load_dotenv

load_dotenv()

tools = [TavilySearchResults(max_results=1)]

tool_executor = ToolExecutor(tools)

model = ChatOpenAI(temperature=0, streaming=True)

functions = [format_tool_to_openai_function(t) for t in tools]

model = model.bind_functions(functions)


inputs = {"messages": [HumanMessage(
    content="what is the weather in sf")], "model": model, "tool_executor": tool_executor}

for output in app.stream(inputs):
    # stream() yields dictionaries with output keyed by node name
    for key, value in output.items():
        print(f"Output from node '{key}':")
        print("---")
        print(value)
    print("\n---\n")
