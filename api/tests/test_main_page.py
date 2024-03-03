import allure
import requests
import pytest
import json

from api import contants, models
from api.client import main_page_api


@allure.epic('Главная страница')
@allure.feature('Работа с пользователями')
class TestMainPage:

    client = requests

    @allure.story('Запросы')
    @allure.title('Получение списка пользователей по странице')
    @pytest.mark.parametrize('page', contants.pages)
    def test_list_users(self, page):
        with allure.step(f'Получаем список пользователей по странице {page}'):
            response = main_page_api.get_list_users(self.client, page)
            list_users = json.loads(response.text)

            assert response.status_code == 200
            assert models.ListUsersModel(**list_users)

    @allure.story('Запросы')
    @allure.title('Получение пользователя по id')
    @pytest.mark.parametrize('user_id', contants.user_ids.keys())
    def test_single_user(self, user_id):
        with allure.step(f'Получаем пользователя по id {user_id}'):
            response = main_page_api.get_single_user(self.client, user_id)
            single_user = json.loads(response.text)

            assert response.status_code == contants.user_ids.get(user_id)
            assert models.SingleUserDataModel(**single_user) if response.status_code == 200 else single_user == {}
