from datetime import datetime
from infrastructure.mcp_client import ObsidianMCPClient
from agno.memory import VectorMemory

class ReviewService:
    def __init__(self, mcp_client: ObsidianMCPClient, memory: VectorMemory):
        self.mcp = mcp_client
        self.memory = memory

    def daily_review(self):
        notes = self.mcp.list_notes()
        report = []
        for note in notes:
            content = self.mcp.read_note(note)
            # lógica: buscar fechas y estado vencido
            if "due_date:" in content:
                # ejemplo simplificado
                report.append({"note": note, "status": "checked"})
        # opcional: actualizar notas con append_content
        return report