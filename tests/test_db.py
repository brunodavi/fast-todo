from sqlalchemy import select

from fast_todo.models import Todo, User


def test_create_user_without_todos(session):
    new_user = User(username='Alice', password='secret', email='test@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'Alice'))

    assert user.username == 'Alice'


def test_create_todo(session, user):
    todo = Todo(
        title='Test Todo',
        description='Test Description',
        state='draft',
        user_id=user.id,
    )

    session.add(todo)
    session.commit()
    session.refresh(todo)

    user = session.scalar(select(User).where(User.id == user.id))

    assert todo in user.todos
