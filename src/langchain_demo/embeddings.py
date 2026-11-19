from langchain_aws import BedrockEmbeddings

from langchain_demo.config import AWS_REGION, EMBEDDING_MODEL_ID


def get_embeddings() -> BedrockEmbeddings:
    return BedrockEmbeddings(model_id=EMBEDDING_MODEL_ID, region_name=AWS_REGION)
