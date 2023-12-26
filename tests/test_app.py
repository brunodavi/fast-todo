from fast_todo.schemas import UserPublic


def test_rota_raiz_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


def test_get_token(client, user):
    response = client.post(
        '/token',
        data={'username': user.email, 'password': user.clean_password},
    )

    token = response.json()

    assert response.status_code == 200
    assert 'access_token' in token
    assert 'token_type' in token


def test_create_user(client):
    response = client.post(
        '/users',
        json={
            'username': 'Geo',
            'email': 'geo@example.com.br',
            'password': 'batatinhas',
        },
    )

    assert response.status_code == 201
    assert response.json() == {
        'id': 1,
        'username': 'Geo',
        'email': 'geo@example.com.br',
    }


def test_create_user_but_username_exists(client, user):
    response = client.post(
        '/users',
        json={
            'username': user.username,
            'email': user.email,
            'password': user.password,
        },
    )

    assert response.status_code == 400
    assert response.json() == {'detail': 'Esse usuário já foi cadastrado'}


def test_get_users(client):
    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() == {'users': []}


def test_get_users_with_users(client, user):
    user_schema = UserPublic.model_validate(user).model_dump()
    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() == {'users': [user_schema]}


def test_update_user(client, user, token):
    response = client.put(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
        json={
            'username': 'new_user',
            'email': 'new@email.com',
            'password': 'new_pass',
        },
    )

    assert response.status_code == 200
    assert response.json() == {
        'id': 1,
        'username': 'new_user',
        'email': 'new@email.com',
    }


def test_delete_user(client, user, token):
    response = client.delete(
        f'/users/{user.id}',
        headers={'Authorization': f'Bearer {token}'},
    )

    assert response.status_code == 200
    assert response.json() == {'detail': 'Usuário deletado'}
