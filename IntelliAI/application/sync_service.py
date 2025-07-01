from agno.memory import VectorMemory
from infrastructure.mcp_client import ObsidianMCPClient
from domain.repositories import NoteRepositoryImpl

class SyncService:
    def __init__(self, mcp_client: ObsidianMCPClient, memory: VectorMemory):
        self.mcp = mcp_client
        self.memory = memory

    def sync_vault(self):
        notes = self.mcp.list_notes()
        for note in notes:
            content = self.mcp.read_note(note)
            self.memory.add(id=note, content=content)