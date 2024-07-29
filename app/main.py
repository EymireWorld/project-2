import os

from fastapi import FastAPI

from app.api.router import router as api_router


app = FastAPI(
    title='EymireNetwork'
)
app.include_router(api_router)


@app.get('/')
def home():
    return {'worker_id': str(os.getpid())}
