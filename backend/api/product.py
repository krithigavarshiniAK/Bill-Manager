from fastapi.routing import APIRouter

router = APIRouter()


@router.get("/customer_info/{customer_name}")
def customer_info(customer_name: str):
    
    return {'Name': customer_name}