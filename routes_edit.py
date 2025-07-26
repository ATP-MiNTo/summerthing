from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from datetime import date
from storage import storage

router = APIRouter()

@router.post("/edit-todo/{todo_id}")
def edit_todo(todo_id: int, item: str = Form(...), due_date: date = Form(...)):
    storage.edit_todo(todo_id, item, due_date)
    return RedirectResponse("/", status_code=303)
