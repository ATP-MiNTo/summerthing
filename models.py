from pydantic import BaseModel
from datetime import date

class Todo(BaseModel):
    id: int
    item: str
    due_date: date
    status: str = "Undone"
