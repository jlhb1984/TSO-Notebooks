from fastapi import APIRouter#
from models import Plan#
from db import session#

router = APIRouter()

@router.post('/plans')
def create_plan(plan_data: Plan):
    plan_db = Plan.model_validate(plan_data.model_dump())
    session.add(plan_db)
    session.commit()
    session.refresh(plan_db)
    return plan_db