from sqlalchemy.orm import Session
from .. import model, schema

# create customer 
def add_customer(db: Session, customer: schema.Customer):
    customerModel = model.Customer(name=customer.name, address=customer.address, phone_no=customer.phone_no, gst_no=customer.gst_no)
    db.add(customerModel)
    db.commit()
    db.refresh(customerModel) 
    return customerModel

# get all customer details
def get_all_customers(db: Session, skip: int = 0, limit: int = 1000):
    return db.query(model.User).offset(skip).limit(limit).all()

# get customer details
def get_customer(db: Session, customer_id: int):
    return db.query(model.Customer).filter(model.Customer.id == customer_id).first()


