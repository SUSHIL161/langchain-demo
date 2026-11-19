from pathlib import Path

from langchain_aws.vectorstores import AmazonS3Vectors
from langchain_core.documents import Document
from langchain_core.embeddings import Embeddings
from langchain_text_splitters import RecursiveCharacterTextSplitter

from langchain_demo.config import S3_VECTOR_BUCKET, S3_VECTOR_INDEX

DATA_DIR = Path(__file__).resolve().parents[2].joinpath("data")


def load_documents() -> list[Document]:
    md_files = sorted(DATA_DIR.glob("*.md"))
    documents: list[Document] = []

    for md_file in md_files:
        md_file_content = md_file.read_text(encoding="utf-8")
        documents.append(
            Document(page_content=md_file_content, metadata={"source": md_file.name})
        )

    return documents


def split_documents(docs: list[Document]) -> list[Document]:
    return RecursiveCharacterTextSplitter(
        chunk_size=500, chunk_overlap=50
    ).split_documents(docs)


def get_vector_store(embeddings: Embeddings) -> AmazonS3Vectors:
    return AmazonS3Vectors(
        vector_bucket_name=S3_VECTOR_BUCKET,
        index_name=S3_VECTOR_INDEX,
        embedding=embeddings,
    )


def index_documents(embeddings: Embeddings) -> int:
    chunks = split_documents(load_documents())
    for i, chunk in enumerate(chunks):
        chunk.id = f"{Path(chunk.metadata['source']).name}-{i}"
    get_vector_store(embeddings).add_documents(chunks)
    return len(chunks)


def get_s3_retriever(embeddings, k=3):
    get_vector_store(embeddings).as_retriever(search_kwargs={"k": k})
