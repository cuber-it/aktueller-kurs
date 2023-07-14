from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import Dict

app = FastAPI()

# In-memory store for data. Typically, this will be replaced with a database
data: Dict[int, Dict] = {}

class Item(BaseModel):
    name: str
    description: str = None

@app.get("/resource")
async def read_resources():
    return data

@app.post("/resource/{id}")
async def create_resource(id: int, item: Item):
    if id in data:
        raise HTTPException(status_code=400, detail="ID already exists")
    data[id] = item.dict()
    return data[id]

@app.get("/resource/{id}")
async def read_resource(id: int):
    if id not in data:
        raise HTTPException(status_code=404, detail="ID not found")
    return data[id]

@app.put("/resource/{id}")
async def update_resource(id: int, item: Item):
    if id not in data:
        raise HTTPException(status_code=404, detail="ID not found")
    data[id] = item.dict()
    return data[id]

@app.patch("/resource/{id}")
async def partial_update_resource(id: int, item: Item):
    if id not in data:
        raise HTTPException(status_code=404, detail="ID not found")
    for key, value in item.dict().items():
        if value is not None:
            data[id][key] = value
    return data[id]

@app.delete("/resource/{id}")
async def delete_resource(id: int):
    if id not in data:
        raise HTTPException(status_code=404, detail="ID not found")
    del data[id]
    return {"detail": "Resource deleted successfully"}
