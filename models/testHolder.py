from pydantic import BaseModel, Field
from datetime import datetime
from bson import ObjectId
from typing import Optional
from models.pyObjectId import PyObjectId

class HolderkData(BaseModel):
    id: PyObjectId = Field(default_factory=PyObjectId, alias="_id")
    rut: str = Field(...)
    name: str = Field(...) 
    lessee: str = Field(...)
    creationDateTime: datetime = datetime.now() 
    modificationDateTime: datetime = datetime.now() 

    class Config:
        allow_population_by_field_name = True
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "rut": "11111111-1",
                "name": "nombre del titular",
                "lessee": "seleccionar",
            }
        }


class UpdateHolderkData(BaseModel):
    HolderId: Optional[int]
    rut: Optional[str]
    name: Optional[str] 
    lessee: Optional[str]
    modificationDateTime: datetime = datetime.now() 
    
    class Config:
        arbitrary_types_allowed = True
        json_encoders = {ObjectId: str}
        schema_extra = {
            "example": {
                "rut": "11111111-1",
                "name": "nombre del titular",
                "lessee": "seleccionar",
            }
        }        