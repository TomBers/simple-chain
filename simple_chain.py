from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

_prompt = ChatPromptTemplate.from_messages(
    [
        (
            "system",
            "You are a helpful AI bot. Your aim is to answer any question as simply as possible.",
        ),
        ("human", "{text}"),
    ]
)
_model = ChatOpenAI()


_output_parser = StrOutputParser()

chain = _prompt | _model | _output_parser
