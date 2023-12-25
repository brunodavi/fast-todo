from fastapi import FastAPI

from fast_todo.schemas import UserPublic, UserSchema, UserDB

app = FastAPI()


@app.get('/')
def read_root():
    return {'message': 'Olá Mundo!'}


fake_database = [] # para estudo


@app.post('/users', status_code=201, response_model=UserPublic)
def create_user(user: UserSchema):
    user_with_id = UserDB(**user.model_dump(), id=len(fake_database) + 1)
    fake_database.append(user_with_id)

    return user_with_id
