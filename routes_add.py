from fastapi import APIRouter, Form
from fastapi.responses import RedirectResponse
from datetime import date
from storage import storage

router = APIRouter()

@router.post("/create-todo")
def create_todo(item: str = Form(...), due_date: date = Form(...)):
    storage.add_todo(item, due_date)
    return RedirectResponse("/", status_code=303)
