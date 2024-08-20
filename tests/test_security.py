from jwt import decode
from fast_zero.security import create_access_token, settings


def test_jwt():
    data = {'sub': 'teste@teste.com'}
    token = create_access_token(data)

    resultado = decode(token, settings.SECRET_KEY, algorithms=[settings.algorithm])

    assert resultado['sub'] == data['sub']
    assert resultado['exp']
