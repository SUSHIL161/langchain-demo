from langchain_aws import ChatBedrockConverse

from langchain_demo.config import AWS_REGION, BEDROCK_MODEL_ID


def get_llm(temperature: float = 0) -> ChatBedrockConverse:
    model = ChatBedrockConverse(
        model=BEDROCK_MODEL_ID, temperature=temperature, region_name=AWS_REGION
    )
    return model
