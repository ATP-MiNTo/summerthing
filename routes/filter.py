
from fastapi import APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.templating import Jinja2Templates
from storage import storage

templates = Jinja2Templates(directory="templates")
router = APIRouter()

@router.get("/done", response_class=HTMLResponse)
def show_done(request: Request):
    todos = storage.get_by_status("Done")
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos, "show_done": True})

@router.get("/undone", response_class=HTMLResponse)
def show_undone(request: Request):
    todos = storage.get_by_status("Undone")
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos, "show_done": False})

@router.get("/upcoming", response_class=HTMLResponse)
def show_upcoming(request: Request):
    todos = storage.get_upcoming()
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos, "upcoming": True})
