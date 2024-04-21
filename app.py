from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Optional, List

app = FastAPI()

class Task(BaseModel):
    id: Optional[int] = None
    title: str
    description: str
    completed: bool = False

tasks = []
task_id_counter = 1

@app.get("/tasks", response_model=List[Task])
async def read_tasks():
    return tasks

@app.get("/tasks/{task_id}", response_model=Task)
async def read_task(task_id: int):
    for task in tasks:
        if task.id == task_id:
            return task
    raise HTTPException(status_code=404, detail="Task not found")

@app.post("/tasks", response_model=Task)
async def create_task(task: Task):
    global task_id_counter
    task.id = task_id_counter
    task_id_counter += 1
    tasks.append(task)
    return task

@app.put("/tasks/{task_id}", response_model=Task)
async def update_task(task_id: int, task_update: Task):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            updated_task = task.copy(update=task_update.dict(exclude_unset=True))
            tasks[index] = updated_task
            return updated_task
    raise HTTPException(status_code=404, detail="Task not found")

@app.delete("/tasks/{task_id}", response_model=Task)
async def delete_task(task_id: int):
    for index, task in enumerate(tasks):
        if task.id == task_id:
            return tasks.pop(index)
    raise HTTPException(status_code=404, detail="Task not found")