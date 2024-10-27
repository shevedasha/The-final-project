import requests
import json
import allure
from Environment import api_URL_1, api_URL_2, access_token


@allure.severity("BLOCKER")
class CartAPI:
    """
    Этот класс представляет сущность - 'Корзина', здесь методы для API-тестирования корзины
    """
    url1 = api_URL_1
    url2 = api_URL_2

    def __init__(self, url):
        self.url = url
        self.headers = {
            'Content-Type': 'application/json',
            'Authorization': access_token
        }

    @allure.step("Добавить книгу в корзину через id {book_id}")
    def add_to_cart(self, book_id: int) -> str:
        """Добавление книги в корзину"""
        data = {
            "id": book_id,
        }
        resp = requests.post(
            self.url1, headers=self.headers, data=json.dumps(data))
        return resp.status_code
    
    @allure.step("Получить список книг в корзине")
    def get_cart(self) -> dict:
        """Получение списка книг в корзине"""
        resp = requests.get(self.url2, headers=self.headers)
        return resp.status_code

    @allure.step("Очистить корзину")
    def clear_cart(self):
        """Очищает корзину"""
        resp = requests.delete(self.url2, headers=self.headers)
        return resp.status_code

    @allure.step("Изменить количество товаров в корзине")
    def update_cart(self, products: dict) -> tuple:
        """Меняет количество товара"""
        response = requests.put(
            self.url2, headers=self.headers, data=json.dumps(products))
        return response.status_code

    @allure.step("Отправитт пустой запрос на добавление товара в корзину")
    def add_empty_request(self, book_id: int) -> str:
        "Добавление товара"
        resp = requests.post(
            self.url1, json={}, headers=self.headers)
        return resp.status_code
