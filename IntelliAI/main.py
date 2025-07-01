from agno.team import Team
from agents.planner_agent import PlannerAgent
from agents.query_agent import QueryAgent
from agents.review_agent import ReviewAgent
from agents.sync_agent import SyncAgent
import subprocess
import threading

# 1. Levantar MCP dummy en hilo separado
def start_dummy_mcp():
    subprocess.run(["python", "-u", "infrastructure/dummy_mcp_server.py"], check=True)

mcp_thread = threading.Thread(target=start_dummy_mcp, daemon=True)
mcp_thread.start()

# 2. Definir el team con triggers activos
def on_vault_change(event):
    # Esta función puede ser vinculada a un watcher de fs o webhook
  dir(memo := SyncAgent.run(event))

team = Team(
    members=[PlannerAgent, QueryAgent, ReviewAgent, SyncAgent],
    instructions=(
        "Coordina el flujo completo de planificación, consultas, revisión y sincronización. "
        "Los agentes responden a triggers configurados: "
        "'create_plan', 'query_notes', 'semantic_search', 'vault_changed', 'daily_review'."
    )
)

if __name__ == "__main__":
    # Iniciar los triggers cronometrados o watchers según sea necesario
    print("Iniciando IntelliAI Agent Team...")
    team.run()  # Corre el ciclo de escucha de intents y eventos