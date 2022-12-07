'''
This file is responsible for creating the model for the database.
This File will have SQLAlchemy models
'''
from sqlalchemy import Column, DateTime, ForeignKey, Integer, String, Float, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func

from db import Base


class Customer(Base):
    __tablename__ = 'customer'

    id  = Column(Integer, primary_key=True, index=True, )
    name = Column(String, unique=True)
    address = Column(String)
    gst_no = Column(String, unique=True)
    phone_no = Column(String)
    email = Column(String)


class Item(Base):
    __tablename__ = "items"

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String, index=True)
    description = Column(String, index=True)
    owner_id = Column(Integer, ForeignKey("customer.id"))

    owner = relationship("Customer", back_populates="items")