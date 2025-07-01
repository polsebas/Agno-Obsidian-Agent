from abc import ABC, abstractmethod
from domain.models import Task

class ITaskRepository(ABC):
    @abstractmethod
    def save(self, task: Task) -> None:
        """Persiste una tarea en el repositorio."""
        pass

class TaskRepositoryImpl(ITaskRepository):
    def __init__(self, memory):
        self.memory = memory

    def save(self, task: Task) -> None:
        # Usa VectorMemory o cualquier otro mecanismo para persistir
        self.memory.add(id=task.id, content=task)

class NoteRepositoryImpl:
    def __init__(self, mcp_client, memory):
        self.mcp = mcp_client
        self.memory = memory

    def list(self) -> list[str]:
        return self.mcp.list_notes()

    def read(self, note_id: str) -> str:
        return self.mcp.read_note(note_id)

    def write(self, note_id: str, content: str) -> None:
        self.mcp.write_note(note_id, content)