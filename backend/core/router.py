from fastapi import APIRouter
from ..api import customer

api_router = APIRouter()

api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
api_router.include_router(customer.router, prefix="/customers", tags=["customers"])
