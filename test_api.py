import allure
import pytest
from Environment import api_URL_1, api_URL_2
from Cart_API import CartAPI

api1 = CartAPI(api_URL_1)
api2 = CartAPI(api_URL_2)

def test_add_to_cart():
    with allure.step("Добавить книгу в корзину по id"):
        book_id = 2980525
        status_code = api1.add_to_cart(book_id)
    with allure.step("Проверить статус запроса"):
        assert status_code == 200

def test_get_cart():
    with allure.step("Показать список товаров в корзине"):
        status_code = api2.get_cart()
    with allure.step("Проверить статус запроса"):
        assert status_code == 200

def test_clear_cart():
    with allure.step("Очистить корзину"):
        status_code = api2.clear_cart()
    with allure.step("Проверить статус запроса"):
        assert status_code == 204

def test_cart_update():
    with allure.step("Изменить количество товара"):
        book_id = 3018590
        api1.add_to_cart(book_id)
        params = [{"id": 150818764, "quantity": 7}]
        status_code = api2.update_cart(params)
    with allure.step("Проверить статус запроса"):
        assert status_code == 200

def test_add_empty_request():
    with allure.step("Добавить книгу в корзину по id"):
        book_id = ''
        status_code = api1.add_empty_request(book_id)
    with allure.step("Проверить статус запроса"):
        assert status_code == 422
