from pymilvus import connections, FieldSchema, CollectionSchema, DataType, Collection

connections.connect("default", host="127.0.0.1", port="19530")

fields = [
    FieldSchema(name="id", dtype=DataType.VARCHAR, is_primary=True, max_length=64),
    FieldSchema(name="embedding", dtype=DataType.FLOAT_VECTOR, dim=1536)
]
schema = CollectionSchema(fields, description="Embeddings de notas Obsidian")
Collection(name="vault_notes", schema=schema)

from agno.vectordb.milvus import Milvus
from agno.memory import VectorMemory

vector_db = Milvus(collection="vault_notes")
memory = VectorMemory(vector_db=vector_db)