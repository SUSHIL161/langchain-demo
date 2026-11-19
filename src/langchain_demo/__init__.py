import sys

from langchain_demo.chains import build_qa_chain
from langchain_demo.embeddings import get_embeddings
from langchain_demo.knowledge_base import get_kb_retriever
from langchain_demo.llm import get_llm
from langchain_demo.rag import RagService
from langchain_demo.s3_vectors import (
    get_s3_retriever,
    index_documents,
)


def main() -> None:
    argument = sys.argv[1:]
    if len(argument) == 0:
        print(
            build_qa_chain().invoke(
                {"role": "Python expert", "question": "What is uv in one line?"}
            )
        )
    else:
        text = " ".join(argument)
        if "--index" in argument:
            index_count = index_documents(get_embeddings())
            print(f"Indexing Done: Total chunks : {index_count} ")
        elif "--kb" in argument:
            rag_text = text.replace("--kb", "").strip()
            rag_service = RagService(get_llm(), get_kb_retriever())
            print(rag_service.ask(rag_text))
        elif "--rag" in argument:
            rag_text = text.replace("--rag", "").strip()
            rag_service = RagService(get_llm(), get_s3_retriever(get_embeddings()))
            print(rag_service.ask(rag_text))
        else:
            print(build_qa_chain().invoke({"role": "Python expert", "question": text}))
