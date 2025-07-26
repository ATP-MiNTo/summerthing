    # ...existing code...

from fastapi import FastAPI, Request, Form
from fastapi.responses import HTMLResponse, RedirectResponse
from fastapi.templating import Jinja2Templates
from fastapi.staticfiles import StaticFiles
from storage import storage
from routes_add import router as add_router
from routes_delete import router as delete_router
from routes_edit import router as edit_router
from routes_filter import router as filter_router

app = FastAPI()
app.mount("/static", StaticFiles(directory="static"), name="static")
templates = Jinja2Templates(directory="templates")

app.include_router(add_router)
app.include_router(delete_router)
app.include_router(edit_router)
app.include_router(filter_router)

@app.get("/", response_class=HTMLResponse)
def read_root(request: Request):
    todos = storage.get_all()
    return templates.TemplateResponse("index.html", {"request": request, "todos": todos, "upcoming": False})

# Support HTML form DELETE for /delete-todo/{todo_id}
@app.post("/delete-todo/{todo_id}")
def delete_todo_form(todo_id: int, method: str = Form(None)):
    if method == "DELETE":
        storage.delete_todo(todo_id)
    return RedirectResponse("/", status_code=303)