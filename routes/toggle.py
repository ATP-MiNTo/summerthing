from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from storage import storage

router = APIRouter()

@router.post("/toggle-todo/{todo_id}")
def toggle_todo(todo_id: int):
    storage.toggle_status(todo_id)
    return RedirectResponse("/", status_code=303)
