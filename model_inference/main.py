from contextlib import asynccontextmanager
from fastapi import FastAPI
from model_inference.router import router as task_router
from model.models import model_loader
# from app.utils.fastapi_globals import g

@asynccontextmanager
async def lifespan(app: FastAPI):
    model_loader.load_model()
    print('loaded model')
    yield
    print('Shutting down the model...')


app = FastAPI(lifespan=lifespan)
app.include_router(task_router)