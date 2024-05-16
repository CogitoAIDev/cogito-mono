from fastapi import APIRouter, Depends, Body

from app.config import logger
from app.users.service import IUserService, get_user_service
from app.users.schemas import (
    UserCreateDTO,
    UserResponseDTO,
    UserUpdateDTO
)

user_router = APIRouter()


@user_router.post(
    '/users/',
    response_model=UserResponseDTO,
    response_model_exclude_none=True
)
async def register_user(
        user_service: IUserService = Depends(get_user_service),
        user_data: UserCreateDTO = Body()
):
    logger.debug(
        f'Inside user.api in register_user with user_data: {user_data}'
    )
    try:
        return await user_service.register_user(user_data)
    except Exception as e:
        logger.error('Something is going wrong... :[')
        logger.exception(e)


@user_router.put(
    '/users/{user_id}',
    response_model=UserResponseDTO,
    response_model_exclude_none=True
)
async def update_user(
    user_service: IUserService = Depends(get_user_service),
    new_user_data: UserUpdateDTO = Body()
):
    logger.debug(f'Inside users.api in update_user with: {new_user_data}')
    try:
        return await user_service.update_user(new_user_data)
    except Exception as e:
        logger.error('Something is going wrong... :[')
        logger.exception(e)
