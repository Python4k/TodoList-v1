from fastapi import APIRouter

from .schemas import SchemaCreateTodo, SchemaUpdateTodo
from .controller import get_todos as controller_get_todos
from .controller import get_todo_by_id as controller_get_todo_by_id
from .controller import create_todo as controller_create_todo
from .controller import update_todo as controller_update_todo
from .controller import delete_todo as controller_delete_todo


router = APIRouter(
    prefix="/todos",
    tags=["Todos"],
    responses={404: {"description": "Not found"}},
)

@router.get("/")
async def get_todos():
    todos = await controller_get_todos()
    return todos

@router.get("/{id}")
async def get_todo_by_id(id: int):
    todo = await controller_get_todo_by_id(id=id)
    return todo

@router.post("/add")
async def create_todo(todo: SchemaCreateTodo):
    todo_model = await controller_create_todo(**todo.model_dump())
    return todo_model

@router.put("/update/{id}")
async def update_todo(id: int, todo: SchemaUpdateTodo):
    todo = await controller_update_todo(id, **todo.model_dump())
    todo_model = await controller_get_todo_by_id(id)
    return todo_model

@router.delete("/delete/{id}" )
async def delete_todo(id: int):
    await controller_delete_todo(id)
    return {"deleted": True}
