from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from agno.vectordb.milvus import Milvus
from agno.agent import Agent, AgentKnowledge
from infrastructure.mcp_client import ObsidianMCPClient

memory_db = SqliteMemoryDb(table_name="agent_memory", db_file="memory.db")
memory = Memory(db=memory_db, model=...)
vector_db = Milvus(collection="vault_notes", uri="127.0.0.1:19530")
knowledge = AgentKnowledge(vector_db=vector_db, add_references=True)

mcp = ObsidianMCPClient(endpoint="http://localhost:5000")

QueryAgent = Agent(
    name="QueryAgent",
    model="gpt-4o",
    memory=memory,
    tools=[mcp],
    instructions=(
        "Si la intención es 'query_notes', usa mcp.list_notes/read_note. "
        "Si es 'semantic_search', realiza embeddings y consulta memoria vectorial."
    ),
    triggers=["on_intent:query_notes", "on_intent:semantic_search"]
)

# QueryAgent = Agent(
#     name="QueryAgent",
#     model=OpenAIChat(id="gpt-4o"),
#     storage=storage,
#     memory=memory,
#     knowledge=knowledge,
#     search_knowledge=True,
#     tools=[mcp],
#     instructions="...",
#     show_tool_calls=True,
#     markdown=False
# )