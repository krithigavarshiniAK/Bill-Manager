'''
It is used to write how an object in a model can be easily mapped using ORM.
This file will have Pydantic models
'''
# build a schema using pydantic
from pydantic import BaseModel

class Customer(BaseModel):
    name: str
    address: str
    gst_no: str
    phone_no: str

    class Config:
        orm_mode = True