import psycopg2

from langchain_community.utilities import SQLDatabase

from langchain.agents import create_sql_agent
from langchain_community.agent_toolkits import SQLDatabaseToolkit
from langchain.agents.agent_types import AgentType
from langchain_openai import ChatOpenAI

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

agent_executor.invoke(
    "looking at the statements, who is the mostlikely suspect?")
