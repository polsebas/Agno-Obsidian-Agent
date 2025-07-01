from dataclasses import dataclass
from datetime import date

@dataclass(frozen=True)
class Task:
    id: str
    title: str
    due_date: date
    status: str  # 'pendiente', 'en-progreso', 'completado'

@dataclass(frozen=True)
class Project:
    id: str
    name: str
    objective: str
    tasks: list[Task]