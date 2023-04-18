from fastapi import APIRouter
from routers.users import router_user

api_router = APIRouter()
api_router.include_router(router_user)
