import allure
import os
from dotenv import load_dotenv

load_dotenv()
base_url = os.getenv('BASE_URL')


def get_list_users(client, page):
    '''Получение списка пользователей по номеру страницы'''
    url = f'{base_url}/api/users'
    params = {'page': page}

    with allure.step(f"Получаем список пользователей со страницы {page}"):
        return client.get(url=url, params=params)


def get_single_user(client, user_id):
    '''Получение пользователя по id'''
    url = f'{base_url}/api/users/{user_id}'

    with allure.step(f"Получаем информацию о пользователе с id={user_id}"):
        return client.get(url=url)


def get_list_unknown(client):
    '''Получение списка unknown'''
    url = f'{base_url}/api/unknown'

    with allure.step(f"Получаем список unknown"):
        return client.get(url=url)


def get_single_unknown(client, unknown_id):
    '''Получение пользователя по id'''
    url = f'{base_url}/api/unknown/{unknown_id}'

    with allure.step(f"Получаем информацию о пользователе с id={unknown_id}"):
        return client.get(url=url)


def create_user(client, name, job):
    '''Добавление пользователя'''
    url = f'{base_url}/api/users'
    body = {
        "name": name,
        "job": job
    }
    with allure.step(f'Добавляем пользователя по имени {name} с должностью {job}'):
        return client.post(url=url, json=body)


def update_user(client, user_id, name, job):
    """Обновление пользователя"""
    url = f"{base_url}/api/users/{user_id}"
    body = {
        "name": name,
        "job": job
    }
    with allure.step(f'Обновляем пользователя с id {user_id}. Новое имя - {name}, новая должность {job}'):
        return client.put(url=url, json=body)


def patch_user(client, user_id, name, job):
    """Обновление пользователя"""
    url = f"{base_url}/api/users/{user_id}"
    body = {
        "name": name,
        "job": job
    }
    with allure.step(f'Обновляем пользователя с id {user_id}. Новое имя - {name}, новая должность {job}'):
        return client.patch(url=url, json=body)


def delete_user(client, user_id):
    """Обновление пользователя"""
    url = f"{base_url}/api/users/{user_id}"
    with allure.step(f'Удаляем пользователя с id {user_id}'):
        return client.delete(url=url)


def register_user(client, email, password):
    """Регистрация пользователя"""
    url = f"{base_url}/api/register"
    body = {
        'email': email,
        'password': password
    }
    with allure.step(f'Регистрируем пользователя с email {email}, и паролем {password}'):
        return client.post(url=url, json=body)


def login_user(client, email, password):
    """Регистрация пользователя"""
    url = f"{base_url}/api/login"
    body = {
        'email': email,
        'password': password
    }
    with allure.step(f'Авторизуемся в системе с email {email}, и паролем {password}'):
        return client.post(url=url, json=body)


def get_users_delayed(client, delay_time):
    '''Получение списка пользователей по номеру страницы'''
    url = f'{base_url}/api/users'
    params = {'delay': delay_time}

    with allure.step(f"Получаем список пользователей со страницы с задержкой в {delay_time}c"):
        return client.get(url=url, params=params)
