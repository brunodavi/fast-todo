from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_todo.database import get_session
from fast_todo.models import User
from fast_todo.schemas import Token
from fast_todo.security import (
    create_access_token,
    get_current_user,
    verify_password,
)

router = APIRouter(prefix='/auth', tags=['auth'])

OAuth2Form = Annotated[OAuth2PasswordRequestForm, Depends()]
Session = Annotated[Session, Depends(get_session)]
CurrentUser = Annotated[User, Depends(get_current_user)]


@router.post('/token', response_model=Token)
def login_for_access_token(
    form_data: OAuth2Form,
    session: Session,
):
    invalid_access = HTTPException(
        status_code=400, detail='Email ou senha incorreto'
    )

    user = session.scalar(select(User).where(User.email == form_data.username))

    if not user:
        raise invalid_access

    if not verify_password(form_data.password, user.password):
        raise invalid_access

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}


@router.post('/refresh_token', response_model=Token)
def refresh_access_token(
    current_user: CurrentUser,
):
    new_access_token = create_access_token(data={'sub': current_user.email})

    return {'access_token': new_access_token, 'token_type': 'bearer'}
