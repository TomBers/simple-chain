from langchain_openai import ChatOpenAI
from langchain.agents import AgentExecutor, create_openai_functions_agent
from langchain_core.prompts import SystemMessagePromptTemplate, PromptTemplate, MessagesPlaceholder, HumanMessagePromptTemplate, ChatPromptTemplate

from langchain_community.utilities.wolfram_alpha import WolframAlphaAPIWrapper
from langchain.agents import load_tools
from dotenv import load_dotenv

import typing
import langchain_core

question = "What is the price of 1kg of gold in GBP?"

load_dotenv()

# For testing directly
wolfram = WolframAlphaAPIWrapper()
# print(wolfram.run(question))

_prompt = ChatPromptTemplate(input_variables=['agent_scratchpad', 'input'],
                             input_types={'chat_history': typing.List[typing.Union[langchain_core.messages.ai.AIMessage, langchain_core.messages.human.HumanMessage, langchain_core.messages.chat.ChatMessage, langchain_core.messages.system.SystemMessage, langchain_core.messages.function.FunctionMessage, langchain_core.messages.tool.ToolMessage]],
                                          'agent_scratchpad': typing.List[typing.Union[langchain_core.messages.ai.AIMessage, langchain_core.messages.human.HumanMessage, langchain_core.messages.chat.ChatMessage, langchain_core.messages.system.SystemMessage, langchain_core.messages.function.FunctionMessage, langchain_core.messages.tool.ToolMessage]]},
                             messages=[SystemMessagePromptTemplate(prompt=PromptTemplate(input_variables=[], template='You are a helpful assistant, but you are terrible at maths. when asked a mathematical question make sure you use a tool')), MessagesPlaceholder(variable_name='chat_history', optional=True), HumanMessagePromptTemplate(prompt=PromptTemplate(input_variables=['input'], template='{input}')), MessagesPlaceholder(variable_name='agent_scratchpad')])


_tools = load_tools(["wolfram-alpha"])

_llm = ChatOpenAI(model="gpt-3.5-turbo-1106")

_agent = create_openai_functions_agent(_llm, _tools, _prompt)

agent_executor = AgentExecutor(agent=_agent, tools=_tools, verbose=True)
