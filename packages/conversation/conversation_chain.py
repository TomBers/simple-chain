from langchain_openai import ChatOpenAI
from langchain.chains import ConversationChain
from langchain.chains.conversation.memory import ConversationBufferMemory
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI()
conversation_chain = ConversationChain(
    llm=llm, memory=ConversationBufferMemory())
