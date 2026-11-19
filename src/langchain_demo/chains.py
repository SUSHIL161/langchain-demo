from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate

from langchain_demo.llm import get_llm


def build_qa_chain():

    prompt = ChatPromptTemplate.from_messages(
        [("system", "You are a helpful {role}."), ("human", "{question}")]
    )
    return prompt | get_llm() | StrOutputParser()
