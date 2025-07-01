from agno.memory import VectorMemory
from infrastructure.mcp_client import ObsidianMCPClient

class QueryService:
    def __init__(self, mcp_client: ObsidianMCPClient, memory: VectorMemory):
        self.mcp = mcp_client
        self.memory = memory

    def list_notes(self) -> list[str]:
        return self.mcp.list_notes()

    def read_note(self, note_id: str) -> str:
        return self.mcp.read_note(note_id)

    def semantic_search(self, query: str, top_k: int = 5) -> list[dict]:
        return self.memory.similarity_search(query, k=top_k)