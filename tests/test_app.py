from fastapi.testclient import TestClient
from fast_todo.app import app


def test_rota_raiz_deve_retornar_200_e_ola_mundo():
  client = TestClient(app)

  response = client.get('/')

  assert response.status_code == 200
  assert response.json() == {'message': 'Olá Mundo!'}


def test_rota_user_deve_retornar_201_e_novo_usuario():
  client = TestClient(app)

  response = client.post(
    '/users',
    json={
      'username': 'Geo',
      'email': 'geo@example.com.br',
      'password': 'batatinhas'
    }
  )

  assert response.status_code == 201
  assert response.json() == {
    'id': 1,
    'username': 'Geo',
    'email': 'geo@example.com.br',
  }
