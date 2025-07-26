from fastapi import APIRouter
from fastapi.responses import RedirectResponse
from storage import storage

router = APIRouter()

@router.delete("/delete-todo/{todo_id}")
def delete_todo(todo_id: int):
    storage.delete_todo(todo_id)
    return RedirectResponse("/", status_code=303)
