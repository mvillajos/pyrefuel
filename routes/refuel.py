from fastapi import APIRouter,  HTTPException
from database import get_all_refuels, create_refuel, get_one_refuel, get_one_refuel_id, delete_refuel, update_refuel
from models import RefuelOp, UpdateRefuel

router = APIRouter()

@router.get('/api/refuels')
async def get_refuels():
      refuels = await get_all_refuels()
      return refuels


@router.post('/api/refuels', response_model=RefuelOp)
async def save_refuel(refuel: RefuelOp):
      dataFound = await get_one_refuel(refuel.fecha, refuel.refuelseq)
      if dataFound:
            # print(dataFound['refuelseq'])
            raise HTTPException(409, f"Refuel with Seq {dataFound['refuelseq']} already exists on this date") 

      response = await create_refuel(refuel.dict())
      if response:
            return response
      raise HTTPException(400, 'Something went wrong')


@router.get('/api/refuels/{id}', response_model=RefuelOp)
async def get_refuel(id: str):
      refuel = await get_one_refuel_id(id)
      if refuel:
            return refuel
      raise HTTPException(404, f"Refuel with ID {id} not found")


@router.put('/api/refuels/{id}', response_model = RefuelOp)
async def put_refuel(id: str, refuel: UpdateRefuel):
      response = await update_refuel(id, refuel)
      if response:
            return response
      raise HTTPException(404, f"Refuel with ID {id} not found")


@router.delete('/api/refuels/{id}')
async def remove_refuel(id: str):
      response = await delete_refuel(id)
      if response:
            return "Successfully deleted refuel"
      raise HTTPException(404, f"Refuel with ID {id} not found")