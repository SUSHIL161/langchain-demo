from langchain_aws.retrievers import AmazonKnowledgeBasesRetriever

from langchain_demo.config import AWS_REGION, KB_ID


def get_kb_retriever(k: int = 3) -> AmazonKnowledgeBasesRetriever:
    return AmazonKnowledgeBasesRetriever(
        knowledge_base_id=KB_ID,
        region_name=AWS_REGION,
        retrieval_config={"managedSearchConfiguration": {"numberOfResults": k}},
    )
