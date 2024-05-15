from fastapi import APIRouter, Depends, Body

user_router = APIRouter()


@user_router.post('/users/')
async def register_user(
        user_service=Depends(),
        user_data=Body()
):
    ...
