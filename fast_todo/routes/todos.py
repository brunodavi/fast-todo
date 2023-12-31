from typing import Annotated

from fast_todo.database import get_session
from fast_todo.models import Todo, User
from fast_todo.schemas import TodoPublic, TodoSchema
from fast_todo.security import get_current_user
from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session

CurrentUser = Annotated[User, Depends(get_current_user)]
Session = Annotated[Session, Depends(get_session)]

router = APIRouter(prefix='/todos', tags=['todos'])


@router.post('/', response_model=TodoPublic)
def create_todo(todo: TodoSchema, user: CurrentUser, session: Session):
    db_todo = Todo(
        title=todo.title,
        description=todo.description,
        state=todo.state,
        user_id=user.id,
    )

    session.add(db_todo)
    session.commit()
    session.refresh(db_todo)

    return db_todo
