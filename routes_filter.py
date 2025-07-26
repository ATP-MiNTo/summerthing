from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from storage import storage

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/upcoming", response_class=HTMLResponse)
def show_upcoming(request: Request):
    todos = storage.get_upcoming()
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos, "upcoming": True})
