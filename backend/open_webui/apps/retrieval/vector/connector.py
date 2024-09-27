from open_webui.apps.retrieval.vector.dbs.chroma import ChromaClient
from open_webui.apps.retrieval.vector.dbs.milvus import MilvusClient


from open_webui.config import VECTOR_DB

if VECTOR_DB == "milvus":
    VECTOR_DB_CLIENT = MilvusClient()
else:
    VECTOR_DB_CLIENT = ChromaClient()
