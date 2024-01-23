from fastapi import FastAPI
from app.apis import apis_router
from tortoise.contrib.fastapi import register_tortoise

app = FastAPI()
app.include_router(apis_router)
# save db to folder databases
register_tortoise(
    app = app,
    db_url="sqlite://todo.db",
    modules={
        "models": ["app.apis.todo.models.todo_model"]
    },
    generate_schemas=True,
    add_exception_handlers=True,
)

@app.get("/")
async def index():
    return {"message": "TonyD API Service"}