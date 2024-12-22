from http import HTTPStatus

from fastapi.testclient import TestClient

from fast_zero.app import app


def test_read_root_deve_retornar_ok_e_ola_mundo():
    client = TestClient(app)  # arrange (organizaçao)
    response = client.get('/')  # act (acao)

    assert response.status_code == HTTPStatus.OK  # assert (validacao)
    assert response.json() == {'message': 'Olá Mundo!'}
