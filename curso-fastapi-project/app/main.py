import zoneinfo
from ..db import SessionDep,create_all_tables
from datetime import datetime
from fastapi import FastAPI,HTTPException,status
from ..models import Customer,CustomerCreate,Transaction,Invoice,CustomerUpdate
from sqlmodel import select
from .routers import customers,transactions

app=FastAPI(lifespan=create_all_tables)
app.include_router(customers.router)
app.include_router(transactions.router)

#security=HTTPBasic()

@app.get("/")
async def root():#credentials:Annotated[HTTPBasicCredentials,Depends(security)]):
    return{"message":"Hola mundo!"}

country_timezones={
    "CO":"America/Bogota",
    "MX":"America/Mexico_City",
    "AR":"America/Argentina/Buenos_Aires",
    "BR":"America/SaoPaulo",
    "PE":"America/Lima",
}

@app.get("/time/{iso_code}")
async def time(iso_code: str):
    iso=iso_code.upper()
    timezone_str=country_timezones.get(iso_code)
    tz=zoneinfo.ZoneInfo(timezone_str)
    return {"time": datetime.now(tz)}

#current_id: int=0

#db_customers:list[Customer]=[]

@app.post("/invoices", response_model=Invoice)
async def create_invoice(invoice_data: Invoice):
    return invoice_data