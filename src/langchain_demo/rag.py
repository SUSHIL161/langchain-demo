from langchain_core.documents import Document
from langchain_core.language_models import BaseChatModel
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.retrievers import BaseRetriever
from langchain_core.runnables import Runnable, RunnablePassthrough

RAG_SYSTEM_PROMPT = """You are an assistant for Team Falcon's internal docs.
Answer the question using only the context below.
If the answer isn't in the context, say "I don't know".
Keep the answer short.

Context:
{context}"""


def format_docs(docs: list[Document]) -> str:
    contents = []
    for doc in docs:
        contents.append(doc.page_content)
    return "\n\n".join(contents)


def build_rag_chain(retriever: BaseRetriever, llm: BaseChatModel) -> Runnable[str, str]:
    prompt = ChatPromptTemplate.from_messages(
        [
            ("system", RAG_SYSTEM_PROMPT),
            ("human", "{question}"),
        ]
    )
    return (
        {"context": retriever | format_docs, "question": RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )


class RagService:
    def __init__(self, llm: BaseChatModel, retriever: BaseRetriever):
        self.llm = llm
        self.retriever = retriever
        self.chain = build_rag_chain(self.retriever, self.llm)

    def ask(self, question: str) -> str:
        return self.chain.invoke(question)
