from fastapi import APIRouter, HTTPException
from model.models import model_loader

from shemas import InputData

model = model_loader.load_model()
router = APIRouter(
    prefix='/tasks',
    tags=['таски']
)

@router.get("/get_response")
async def get_response(
    input_: InputData 
)-> dict:
    try:
        response = model(input_)
        return {'response': response}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))


# @router.get("")
# async def get_tasks() -> list[STask]:
#     tasks = await TaskRepository.find_all()
#     return {'data': tasks}