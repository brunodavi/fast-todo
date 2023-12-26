from fastapi import Depends, FastAPI, HTTPException
from fastapi.security import OAuth2PasswordRequestForm
from sqlalchemy import select
from sqlalchemy.orm import Session

from fast_todo.database import get_session
from fast_todo.models import User
from fast_todo.schemas import Message, Token, UserList, UserPublic, UserSchema
from fast_todo.security import (
    create_access_token,
    get_current_user,
    get_password_hash,
    verify_password,
)

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


@app.post('/token', response_model=Token)
def login_for_access_token(
    form_data: OAuth2PasswordRequestForm = Depends(),
    session: Session = Depends(get_session),
):
    invalid_access = HTTPException(
        status_code=400, detail='Email ou senha inválido'
    )

    user = session.scalar(select(User).where(User.email == form_data.username))

    if not user:
        raise invalid_access

    if not verify_password(form_data.password, user.password):
        raise invalid_access

    access_token = create_access_token(data={'sub': user.email})

    return {'access_token': access_token, 'token_type': 'bearer'}


@app.post('/users', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema, session: Session = Depends(get_session)):
    db_user = session.scalar(
        select(User).where(User.username == user.username)
    )

    if db_user:
        raise HTTPException(
            status_code=400, detail='Esse usuário já foi cadastrado'
        )

    hashed_password = get_password_hash(user.password)

    db_user = User(
        email=user.email,
        username=user.username,
        password=hashed_password,
    )

    session.add(db_user)
    session.commit()
    session.refresh(db_user)

    return db_user


@app.get('/users', status_code=200, response_model=UserList)
def get_users(
    skip: int = 0, limit: int = 100, session: Session = Depends(get_session)
):
    users = session.scalars(select(User).offset(skip).limit(limit)).all()
    return {'users': users}


@app.put('/users/{user_id}', status_code=200, response_model=UserPublic)
def update_user(
    user_id: int,
    user: UserSchema,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(status_code=400, detail='Permissões insuficientes')

    current_user.username = user.username
    current_user.password = user.password
    current_user.email = user.email

    session.commit()
    session.refresh(current_user)

    return current_user


@app.delete('/users/{user_id}', response_model=Message)
def delete_user(
    user_id: int,
    session: Session = Depends(get_session),
    current_user: User = Depends(get_current_user),
):
    if current_user.id != user_id:
        raise HTTPException(status_code=400, detail='Permissões insuficientes')

    session.delete(current_user)
    session.commit()

    return {'detail': 'Usuário deletado'}
