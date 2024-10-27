from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.common.keys import Keys
from Environment import ui_URL

@allure.severity("BLOCKER")
class Cart:
    """
    Этот класс представляет сущность - 'Корзина', здесь методы для тестирования корзины
    """
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get(ui_URL)

    @allure.step("Найти книгу по автору {book_author}")
    def search_book_title(self, book_author: str) -> None:
        """Поиск книги"""
        self.driver.find_element(
            By.CSS_SELECTOR, "[name='phrase']").send_keys(
            book_author, Keys.RETURN)

    @allure.step("Перейти на страницу книги")
    def product_card(self):
        """Переход на страницу книги"""
        self.driver.find_element(
            By.XPATH, "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/div[1]/div[1]/div[1]/div[1]/section[1]/section[1]/div[1]/article[1]/a[1]/picture[1]/img[1]").click()

    @allure.step("Добавить книгу в корзину")
    def add_to_cart(self):
        """Добавление книги в корзину"""
        self.driver.find_element(
            By.XPATH,
            "/html[1]/body[1]/div[2]/div[1]/div[1]/div[3]/main[1]/div[1]/div[6]/div[2]/div[1]/div[1]/div[2]/button[1]").click()
        self.driver.find_element(By.CSS_SELECTOR, "a[href='/cart']").click()

    @allure.step("Удалить книгу из корзины")
    def delete_from_cart(self):
        """Удаление книги"""
        self.driver.find_element(By.CSS_SELECTOR, ".cart-item__actions-icon").click()
