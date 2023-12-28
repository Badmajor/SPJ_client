import requests


def get_token() -> str:
    """
    Receives login and password from .env. Makes a request to the server and receives a token.
    :return: TOKEN
    """
    from decouple import config
    username = config('LOGIN_FOR_SERVER')
    password = config('PASSWORD_FOR_SERVER')
    url_server = config('SERVER_URL')
    url = f'{url_server}api-token-auth/'
    response = requests.post(
        url,
        data={
            'username': username,
            'password': password,
        }
    )
    token = response.json().get('token')
    return token