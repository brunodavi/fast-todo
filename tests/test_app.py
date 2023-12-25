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


def test_get_users(client):
    response = client.get('/users')

    assert response.status_code == 200
    assert response.json() == {
        'users': [
            {
                'username': 'Geo',
                'email': 'geo@example.com.br',
                'id': 1,
            }
        ]
    }


def test_update_user(client):
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
        'username': 'new_user',
        'email': 'new@email.com',
        'id': 1,
    }


def test_delete_user(client):
    response = client.delete('/users/1')

    assert response.status_code == 200
    assert response.json() == {'detail': 'Usuário deletado'}
