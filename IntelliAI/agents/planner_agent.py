# agents/planner_agent.py
from agno.agent import Agent, AgentKnowledge
from agno.vectordb.milvus import Milvus
from application.planner_service import PlannerService
from infrastructure.mcp_client import ObsidianMCPClient
from domain.repositories import TaskRepositoryImpl
from agno.memory.v2.memory import Memory
from agno.memory.v2.db.sqlite import SqliteMemoryDb
from infrastructure.mcp_client import ObsidianMCPClient

memory_db = SqliteMemoryDb(table_name="agent_memory", db_file="memory.db")
memory = Memory(db=memory_db, model=...)
vector_db = Milvus(collection="vault_notes", uri="127.0.0.1:19530")
knowledge = AgentKnowledge(vector_db=vector_db, add_references=True)
mcp = ObsidianMCPClient(endpoint="http://localhost:5000")
vector_db = Milvus(
    collection="recipes",
    uri="./milvus.db",
)
repo = TaskRepositoryImpl(memory)
service = PlannerService(repo=repo)

PlannerAgent = Agent(
    name="PlannerAgent",
    model="gpt-4o",
    memory=memory,
    tools=[mcp],
    instructions=(
        "Desglosa el Project recibido en tareas. "
        "Para cada Task, genera un Markdown con front-matter YAML y llama a mcp.write_note."
    ),
    triggers=["on_intent:create_plan"],
    run=lambda project: service.create_tasks(project)
)
