from fastapi import FastAPI
from pydantic import BaseModel
from app.database.db_func import DBFunction
from app.config import config
from fastapi.middleware.cors import CORSMiddleware


app=FastAPI()
db=DBFunction(config)
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"], # Разрешаем все домены (для разработки)
    allow_methods=["*"], # Разрешаем все методы (POST, GET...)
    allow_headers=["*"],
)
class Auth(BaseModel):
    name:str
    tel:str
    address:str

@app.post("/api/checkout")
async def create_acc(acc:Auth):
    table_name="users"
    columns=["full_name","phone_number","address"]
    values=[acc.name,acc.tel,acc.address]
    await db.set_data(table_name,columns,values)

    return{"message":"Заказ создан"}

