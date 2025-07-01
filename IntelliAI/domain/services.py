from domain.models import Task
from domain.repositories import ITaskRepository
from datetime import datetime

class TaskDomainService:
    """
    Lógica de negocio relacionada con Task:
    - Validaciones de fecha
    - Reglas de estado
    """
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def validate_and_save(self, task: Task) -> None:
        if task.due_date < datetime.now().date():
            raise ValueError("La fecha de vencimiento no puede ser anterior a hoy.")
        if task.status not in ('pendiente', 'en-progreso', 'completado'):
            raise ValueError(f"Estado inválido: {task.status}")
        self.repo.save(task)