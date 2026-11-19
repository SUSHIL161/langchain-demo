import os

from dotenv import load_dotenv

load_dotenv()
AWS_REGION = os.getenv("AWS_REGION", "us-west-2")
BEDROCK_MODEL_ID = os.getenv(
    "BEDROCK_MODEL_ID", "us.anthropic.claude-haiku-4-5-20251001-v1:0"
)
EMBEDDING_MODEL_ID = os.getenv("EMBEDDING_MODEL_ID", "amazon.titan-embed-text-v2:0")
S3_VECTOR_BUCKET = os.getenv("S3_VECTOR_BUCKET", "falcon-docs-vectors-sushil")
S3_VECTOR_INDEX = os.getenv("S3_VECTOR_INDEX", "falcon-docs-titan")
KB_ID = os.getenv("KB_ID", "LE7Z3V1LOA")
