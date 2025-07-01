# agents/review_agent.py
from agno.agent import Agent
from agno.memory import VectorMemory
from infrastructure.mcp_client import ObsidianMCPClient
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.vectordb.milvus import Milvus
from agno.agent import Agent, AgentKnowledge
from infrastructure.mcp_client import ObsidianMCPClient

mcp = ObsidianMCPClient(endpoint="http://localhost:5000")
memory_db = SqliteMemoryDb(table_name="agent_memory", db_file="memory.db")
memory = Memory(db=memory_db, model=...)
vector_db = Milvus(collection="vault_notes", uri="127.0.0.1:19530")
knowledge = AgentKnowledge(vector_db=vector_db, add_references=True)


ReviewAgent = Agent(
    name="ReviewAgent",
    model="gpt-4o",
    memory=memory,
    tools=[mcp],
    instructions=(
        "Cada día (o al dispararse cron), recupera todas las notas, "
        "evalúa fechas y estado, y actualiza front-matter o secciones de contenido según sea necesario."
    ),
    triggers=["cron:daily_review"]
)
