import pytest
from fastapi.testclient import TestClient
from sqlalchemy import StaticPool, create_engine
from sqlalchemy.orm import sessionmaker

from fast_todo.app import app
from fast_todo.database import get_session
from fast_todo.models import Base, User
from fast_todo.security import get_password_hash


@pytest.fixture
def session():
    engine = create_engine(
        'sqlite:///:memory:',
        connect_args={'check_same_thread': False},
        poolclass=StaticPool,
    )

    Session = sessionmaker(bind=engine)
    Base.metadata.create_all(engine)

    yield Session()

    Base.metadata.drop_all(engine)


@pytest.fixture
def client(session):
    def get_session_override():
        return session

    with TestClient(app) as client:
        app.dependency_overrides[get_session] = get_session_override
        yield client

    app.dependency_overrides.clear()


@pytest.fixture
def user(session):
    user = User(
        username='Geo',
        email='geo@example.com.br',
        password=get_password_hash('secret'),
    )

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = 'secret'

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )

    json = response.json()
    return json['access_token']
