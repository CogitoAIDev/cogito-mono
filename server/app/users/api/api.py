from typing import Optional

from fastapi import APIRouter, Depends, Body, Query, HTTPException, status

from app.config import logger
from app.users.exceptions import UserNotFound
from app.users.service import IUserService, get_user_service
from app.users.schemas import (
    EmailRegisterDTO,
    TelegramRegisterDTO,
    UserResponseDTO,
    UserUpdateDTO
)

user_router = APIRouter()


@user_router.post(
    '/register/email',
    response_model=UserResponseDTO,
    response_model_exclude_none=True
)
async def register_user_by_email(
    user_service: IUserService = Depends(get_user_service),
    user_email_data: Optional[EmailRegisterDTO] = Body()
):
    logger.debug(
        f'Inside user.api in register with email with user_data: {user_email_data}'
    )
    try:
        return await user_service.register_user_by_email(user_email_data)
    except Exception as e:
        logger.error('Something is going wrong... :[')
        logger.exception(e)


@user_router.post(
    '/register/telegram',
    response_model=UserResponseDTO,
    response_model_exclude_none=True
)
async def register_user_by_telegram_user_id(
    user_service: IUserService = Depends(get_user_service),
    user_telegram_data: Optional[TelegramRegisterDTO] = Body()
):
    logger.debug(
        f'Inside user.api in register with tg_user_id with user_data: {user_telegram_data}'
    )
    try:
        return await user_service.register_user_by_telegram_user_id(user_telegram_data)
    except Exception as e:
        logger.error('Something is going wrong... :[')
        logger.exception(e)


@user_router.get(
    '/users/',
    response_model=list[UserResponseDTO],
    response_model_exclude_none=True
)
async def find_users_by_ids(
    user_service: IUserService = Depends(get_user_service),
    user_ids: str = Query(None, description='Return users by ids'),
):
    if user_ids:
        try:
            user_ids = list(map(int, user_ids.split(',')))
        except ValueError as e:
            logger.error(
                f'Wrong query string for user_ids, example: user_ids=1,2,3,4,5'
            )
            logger.exception(e)
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail="Wrong query string for user_ids, example: user_ids=1,2,3,4,5"
            )

    logger.debug(
        f'Inside users.api in find users by ids with user_ids: {user_ids}')
    try:
        return await user_service.find_users_by_ids(user_ids)
    except Exception as e:
        logger.error('Something is going wrong... :[')
        logger.exception(e)


@user_router.get(
    '/users/{user_id}',
    response_model=UserResponseDTO,
    response_model_exclude_none=True
)
async def find_user_by_id(
    user_id: int,
    user_service: IUserService = Depends(get_user_service)
):
    logger.debug(
        f'Inside users.api in find user by id with user_id: {user_id}')
    try:
        return await user_service.find_user_by_id(user_id)

    except UserNotFound as e:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=str(e)
        )


@user_router.put(
    '/users/{user_id}',
    response_model=UserResponseDTO,
    response_model_exclude_none=True
)
async def update_user(
    user_id,
    user_service: IUserService = Depends(get_user_service),
    new_user_data: UserUpdateDTO = Body()
):
    logger.debug(f'Inside users.api in update_user with: {new_user_data}')
    try:
        return await user_service.update_user(user_id, new_user_data)
    except Exception as e:
        logger.error('Something is going wrong... :[')
        logger.exception(e)
