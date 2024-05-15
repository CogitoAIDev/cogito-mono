from fastapi import APIRouter, Depends
from fastapi.security import OAuth2PasswordRequestForm

from app.auth.schemas import Token
from app.auth.service import IAuthService


auth_router = APIRouter()


@auth_router.post('/token/', response_model=Token)
async def login(
    auth_service: IAuthService = Depends(),
    form_data: OAuth2PasswordRequestForm = Depends()
):
    '''
    Check, if user exist and generate JWT token for him
    '''
    username = form_data.username
    # password = form_data.password
    access_token = auth_service.create_access_token(data={"sub": username})
    return {"access_token": access_token, "token_type": "bearer"}
