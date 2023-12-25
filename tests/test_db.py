from sqlalchemy import select

from fast_todo.models import User


def test_create_user(session):
    new_user = User(username='Alice', password='secret', email='test@test')
    session.add(new_user)
    session.commit()

    user = session.scalar(select(User).where(User.username == 'Alice'))

    assert user.username == 'Alice'
