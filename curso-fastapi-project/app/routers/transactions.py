from fastapi import APIRouter,HTTPException,status
from ...models import Customer,Transaction,TransactionCreate
from ...db import SessionDep
from sqlmodel import select

router=APIRouter()

@router.post("/transactions",tags=["transactions"])
async def create_transaction(transaction_data: Transaction,session:SessionDep):
    transaction_data_dict=transaction_data.model_dump()
    customer=session.get(Customer,transaction_data_dict.get("customer_id"))
    if not customer:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND)

    transaction_db=Transaction.model_validate(transaction_data_dict)
    session.add(transaction_db)
    session.commit()
    session.refresh()
    return transaction_data

@router.get("/transactions",tags=["transactions"])

async def list_transaction(session:SessionDep):
    query=select(Transaction)
    transactions=session.exec(query).all()
    return transactions