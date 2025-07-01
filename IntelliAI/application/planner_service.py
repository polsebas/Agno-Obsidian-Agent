from domain.models import Project, Task
from domain.repositories import ITaskRepository
from datetime import date

class PlannerService:
    def __init__(self, repo: ITaskRepository):
        self.repo = repo

    def create_tasks(self, project: Project) -> list[Task]:
        # Lógica para desglosar objetivos en tareas con fechas y persistirlas
        tasks = []
        for idx, item in enumerate(project.tasks, start=1):
            task = Task(
                id=f"{project.id}-T{idx}",
                title=item.title,
                due_date=item.due_date,
                status="pendiente",
            )
            self.repo.save(task)
            tasks.append(task)
        return tasks