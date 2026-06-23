import json
from dataclasses import dataclass
from typing import List

@dataclass
class CodingTask:
    id: int
    code: str
    domain: str

class Model:
    def __init__(self):
        self.tasks = []

    def train(self, tasks: List[CodingTask]):
        self.tasks = tasks

    def fine_tune(self, domain: str):
        self.tasks = [task for task in self.tasks if task.domain == domain]

    def update(self, new_tasks: List[CodingTask]):
        # Remove existing tasks with the same id before updating
        self.tasks = [task for task in self.tasks if task.id not in [new_task.id for new_task in new_tasks]]
        self.tasks.extend(new_tasks)

    def get_tasks(self):
        return self.tasks

    def save(self, filename: str):
        with open(filename, 'w') as f:
            json.dump([task.__dict__ for task in self.tasks], f)

    @classmethod
    def load(cls, filename: str):
        with open(filename, 'r') as f:
            tasks = json.load(f)
            model = cls()
            model.tasks = [CodingTask(**task) for task in tasks]
            return model
