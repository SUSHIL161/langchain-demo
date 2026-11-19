from langchain_core.documents import Document
from langchain_core.embeddings import FakeEmbeddings
from langchain_core.language_models import FakeListChatModel
from langchain_core.vectorstores import InMemoryVectorStore

from langchain_demo.rag import RagService, format_docs
from langchain_demo.s3_vectors import load_documents, split_documents


def test_load_documents_returns_three_files():
    docs = load_documents()
    assert len(docs) == 3


def test_split_documents_respects_chunk_size():
    docs = load_documents()
    documents = split_documents(docs)
    print(len(documents))
    assert len(documents) > 3
    for doc in documents:
        assert len(doc.page_content) <= 500


def test_format_docs_joins_with_blank_line():
    docs = list[Document]()
    docs.append(Document(page_content="A"))
    docs.append(Document(page_content="B"))
    assert format_docs(docs) == "A\n\nB"

    print("test")


def test_rag_service_ask_returns_llm_answer():
    chat_model = FakeListChatModel(responses=["Testing"])

    answer = RagService(chat_model, get_vectors().as_retriever()).ask("who are you?")
    assert answer == "Testing"


def get_vectors() -> InMemoryVectorStore:
    vector_store = InMemoryVectorStore(FakeEmbeddings(size=1024))
    vector_store.add_documents(
        [
            Document(page_content="Releases go out Thursday"),
            Document(page_content="Sushil is on-call for this week"),
        ]
    )
    return vector_store
