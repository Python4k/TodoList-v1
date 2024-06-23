from fastapi import Depends, FastAPI, APIRouter, Request
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from fastapi.templating import Jinja2Templates

from .todos.view import get_todos, get_todo_by_id, create_todo, update_todo, delete_todo

from .todos.view import router as todos_router

# API router for api
api = APIRouter(
    prefix="/api"
)

api.include_router(todos_router)

# FastAPI app for jinja
app = FastAPI(
    title="Todo List API",
    version="0.1.0",
    description="A simple Todo List API",
    contact={
        "name": "Python4K",
        "url": "https://github.com/python4k",
    }
)
app.mount("/static", StaticFiles(directory="app/static"), name="static")
templates = Jinja2Templates(directory="app/templates")

@app.get("/", response_class=HTMLResponse)
async def main_page(request: Request):
    return templates.TemplateResponse("base.html", {"request": request})

@app.get("/todos", response_class=HTMLResponse)
async def todos_page(request: Request, todos=Depends(get_todos)):
    return templates.TemplateResponse("todos.html", {"request": request, "todos": todos})

@app.get("/todos/{id}", response_class=HTMLResponse)
async def todo_page(request: Request, id: int, todo=Depends(get_todo_by_id)):
    return templates.TemplateResponse("todo.html", {"request": request, "todo": todo})


app.include_router(api)
