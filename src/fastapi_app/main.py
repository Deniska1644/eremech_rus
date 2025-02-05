from fastapi import FastAPI
import uvicorn

from routers.task_router import router as task_router
from routers.auth import router as auth_router

app = FastAPI(title='tasks')

app.include_router(task_router)
app.include_router(auth_router)

if __name__ == '__main__':
    uvicorn.run(
        app=app,
        host='0.0.0.0',
        port=8000,
    )
