from fastapi import APIRouter, Path, Query, Body, Depends, HTTPException
from .schemas.todo_schemas import GetTodo, PostTodo, PutTodo
from .models.todo_model import Todo

todo_router = APIRouter(prefix="/toDo", tags=["toDo"])

@todo_router.get("/")
async def all_todos():
    data = Todo.all()
    return await GetTodo.from_queryset(data)

@todo_router.post("/")
async def post_todo(body: PostTodo):
    row = await Todo.create(**body.dict(exclude_unset=True))
    return await GetTodo.from_tortoise_orm(row)

@todo_router.put("/{todo_id}")
async def update_todo(todo_id: int, body: PutTodo):
    data = body.dict(exclude_unset=True)
    exists = await Todo.filter(id=todo_id).exists()
    if not exists:
        raise HTTPException(status_code=404, detail="Todo not found")
    await Todo.filter(id=todo_id).update(**data)
    return await GetTodo.from_queryset_single(Todo.get(id=todo_id))

@todo_router.delete("/{todo_id}")
async def delete_todo(todo_id: int):
    exists = await Todo.filter(id=todo_id).exists()
    if not exists:
        raise HTTPException(status_code=404, detail="Todo not found")
    await Todo.filter(id=todo_id).delete()
    return {"message": "Todo deleted successfully"}