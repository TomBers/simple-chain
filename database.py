import psycopg2

from langchain_community.utilities import SQLDatabase

from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage

from dotenv import load_dotenv

load_dotenv()


db = SQLDatabase.from_uri(
    'postgresql+psycopg2://postgres:postgres@localhost:5432/sqlhelper_dev_clean')

# print(db.dialect)
# print(db.get_usable_table_names())
# print(db.run("SELECT * FROM suspects;"))


llm = ChatOpenAI(model="gpt-4-1106-preview", temperature=0)
agent_executor = create_sql_agent(
    llm=llm,
    toolkit=SQLDatabaseToolkit(db=db, llm=llm),
    verbose=True,
    agent_type=AgentType.ZERO_SHOT_REACT_DESCRIPTION,
)

prompt = ChatPromptTemplate.from_messages(
    [
        SystemMessage(
            content="Make sure you look statements table especially statements_text column, this contains eye witness testimony and is key to solving the crime."),
        HumanMessage(
            content="{input}")
    ]
)

agent_executor.invoke({"input": "Who is the most likely suspect?"})
