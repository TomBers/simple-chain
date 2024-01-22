from langchain import hub
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain.agents import tool
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_community.tools import WikipediaQueryRun
from langchain_community.utilities import WikipediaAPIWrapper
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()


@tool
def get_word_length(word: str) -> int:
    """Returns the length of a word."""
    return len(word)


api_wrapper = WikipediaAPIWrapper(top_k_results=1, doc_content_chars_max=500)

tools = [TavilySearchResults(max_results=1),
         WikipediaQueryRun(api_wrapper=api_wrapper), get_word_length]

prompt = hub.pull("hwchase17/openai-functions-agent")

print(prompt.messages)

llm = ChatOpenAI(model="gpt-3.5-turbo-1106")

agent = create_openai_functions_agent(llm, tools, prompt)

agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

agent_executor.invoke(
    {"input": "What is the length of this word? Today"})
