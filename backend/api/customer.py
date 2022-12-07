from fastapi import Depends
from sqlalchemy.orm import Session
from fastapi.routing import APIRouter
from fastapi_sqlalchemy import db

from database.schema import Customer as CustomerSchema
from database.schema import Customer as CustomerModel
from database.db import get_db

router = APIRouter()

@router.post('/add_customer/', response_model=CustomerSchema)
async def add_customer(customer: CustomerSchema, db: Session = Depends(get_db)):
    db_customer = CustomerModel(name=customer.name, address=customer.address, phone_no=customer.phone_no, gst_no=customer.gst_no)
    db.session.add(db_customer)
    db.session.commit()
    return db_customer


@router.get('/get_all_customer/')
async def get_all_customer(db: Session = Depends(get_db)):
    customers = db.session.query(CustomerModel).all()
    return customers


@router.get("/customer_info/{customer_name}")
def customer_info(customer_name: str):
    customer = db.session.query(CustomerModel).filter(CustomerModel.name == customer_name)
    return customer














