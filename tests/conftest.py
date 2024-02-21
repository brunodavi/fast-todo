import pytest
from fastapi.testclient import TestClient
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from fast_todo.app import app
from fast_todo.database import get_session
from fast_todo.models import Base
from fast_todo.security import get_password_hash
from fast_todo.settings import Settings
from tests.factories import UserFactory

settings = Settings()


@pytest.fixture
def session():
    engine = create_engine(settings.DATABASE_URL)

    Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)
    Base.metadata.create_all(engine)

    with Session() as session:
        yield session
        session.rollback()

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
    password = 'test12345'
    user = UserFactory(password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password

    return user


@pytest.fixture
def user2(session):
    password = 'test12345'
    user = UserFactory(id=2, password=get_password_hash(password))

    session.add(user)
    session.commit()
    session.refresh(user)

    user.clean_password = password

    return user


@pytest.fixture
def token(client, user):
    response = client.post(
        '/auth/token',
        data={'username': user.email, 'password': user.clean_password},
    )

    json = response.json()
    return json['access_token']
