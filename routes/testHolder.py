from fastapi import APIRouter, Body, HTTPException, status, Depends
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder
from typing import Optional, List
from config.db import conn
from models.testHolder import HolderkData, UpdateHolderkData
from starlette.status import HTTP_204_NO_CONTENT

testHolder = APIRouter()

@testHolder.get("/api/v1/holder", response_description="List all data of devices", response_model=List[HolderkData], tags=["Holder Data"])
def list_holder_data():
    holder_data = list(conn.holder_data.find())
    return holder_data


@testHolder.post("/api/v1/holder", response_description="Add new data of a device", response_model=HolderkData, tags=["Holder Data"])
def create_holder_data(holder_data: HolderkData):
    holder_data = jsonable_encoder(holder_data)
    new_holder_data = conn.holder_data.insert_one(holder_data)
    created_holder_data = conn.holder_data.find_one({"_id": new_holder_data.inserted_id})
    return JSONResponse(status_code=status.HTTP_201_CREATED, content=created_holder_data)


@testHolder.get("/api/v1/holder/{id}", response_description="Get a single data of a device", response_model=HolderkData, tags=["Holder Data"])
def show_holder_data(id: str):
    if (holder_data := conn.holder_data.find_one({"_id": id})) is not None:
        return holder_data
    raise HTTPException(status_code=404, detail=f"Data {id} not found")


@testHolder.put("/api/v1/holder/{id}", response_description="Update data of a device", response_model=HolderkData, tags=["Holder Data"])
def update_holder_data(id: str, holder_data: UpdateHolderkData = Body(...)):
    holder_data = {k: v for k, v in holder_data.dict().items() if v is not None}
    if len(holder_data) >= 1:
        update_result = conn.holder_data.update_one({"_id": id}, {"$set": holder_data})

        if update_result.modified_count == 1:
            if (
                updated_holder_data:= conn.holder_data.find_one({"_id": id})
            ) is not None:
                return updated_holder_data

    if (existing_holder_data := conn.holder_data.find_one({"_id": id})) is not None:
        return existing_holder_data
    raise HTTPException(status_code=404, detail=f"holder_data {id} not found")


@testHolder.delete("/api/v1/holder/{id}", response_description="Delete data of a device", tags=["Holder Data"])
def delete_holder_data(id: str):
    delete_result = conn.holder_data.delete_one({"_id": id})
    if delete_result.deleted_count == 1:
        return JSONResponse(status_code=status.HTTP_204_NO_CONTENT)
    raise HTTPException(status_code=404, detail=f"Data {id} not found")