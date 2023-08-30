from pydantic import BaseModel, Field , validator
from typing import Optional
from bson import ObjectId
from datetime import datetime

class PyObjectId(ObjectId):
    @classmethod
    def __get_validators__(cls):
        yield cls.validate

    @classmethod
    def validate(cls, v):
        if not ObjectId.is_valid(v):
            raise ValueError('Invalid ObjectId')
        return str(v)

class RefuelOp(BaseModel):
    #id: Optional[PyObjectId] = Field(alias='_id')
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    fecha: str
    refuelseq: Optional[int] = 1
    #created_at: str = Field(default_factory= datetime.now().strftime('%H%M%S'))
    importe: int
    precio_litro: Optional[float]
    litros: float
    totkm: int

    @validator("refuelseq", pre=True, always=True)
    def set_refuelseq(cls, refuelseq):
        return refuelseq or 1

    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}

class UpdateRefuel(BaseModel):
    importe: Optional[int] = None
    precio_litro: Optional[float] = None
    litros: Optional[float] = None
    totkm: Optional[int] = None
    
    class Config:
        orm_mode = True
        allow_population_by_field_name = True
        json_encoders = {ObjectId: str}