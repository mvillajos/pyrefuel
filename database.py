from motor.motor_asyncio import AsyncIOMotorClient
from models import RefuelOp
from bson import ObjectId
from decouple import config

client = AsyncIOMotorClient(config('SRV_MONGO') )
database = client.refueldb
collection = database.refueldata

async def get_one_refuel_id(id):
    refuel = await collection.find_one({'_id': ObjectId(id)})
    return refuel

async def get_one_refuel(fecha, refuelseq):
    refuel = await collection.find_one({'fecha': fecha, 'refuelseq': refuelseq})
    return refuel

async def get_all_refuels():
    refuels = []
    cursor = collection.find({})
    async for document in cursor:
        refuels.append(RefuelOp(**document))
    return refuels


async def create_refuel(refuel):
    new_refuel = await collection.insert_one(refuel)
    created_refuel = await collection.find_one({'_id': new_refuel.inserted_id})
    return created_refuel

async def update_refuel(id: str, data):
    refuel = {k:v for k,v in data.dict().items() if v is not None}
    print(refuel)
    new_refuel = await collection.update_one({'_id': ObjectId(id)}, {'$set': refuel})
    document = await collection.find_one({'_id': ObjectId(id)})
    return document

async def delete_refuel(id: str):
    await collection.delete_one({'_id': ObjectId(id)})
    return True
