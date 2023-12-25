from fast_todo.schemas import UserPublic


def test_rota_raiz_deve_retornar_200_e_ola_mundo(client):
    response = client.get('/')

    assert response.status_code == 200
    assert response.json() == {'message': 'Olá Mundo!'}


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


def test_update_user(client, user):
    response = client.put(
        '/users/1',
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


def test_update_user_but_user_not_found(client):
    response = client.put(
        '/users/1',
        json={
            'username': 'new_user',
            'email': 'new@email.com',
            'password': 'new_pass',
        },
    )

    assert response.status_code == 404
    assert response.json() == {'detail': 'Usuário não encontrado'}


def test_delete_user(client, user):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'Usuário deletado'}


def test_delete_user_but_user_not_found(client):
    response = client.delete('/users/1')

    assert response.status_code == 404
    assert response.json() == {'detail': 'Usuário não encontrado'}
