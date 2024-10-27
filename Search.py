from selenium import webdriver
from selenium.webdriver.common.by import By
import allure
from selenium.webdriver.common.keys import Keys
from Environment import ui_URL

@allure.severity("Major")

class Search:
    """
    Этот класс преставляет сущность - "Строка поиска", тут методы для тестирования строки
    """
    def __init__(self, driver: webdriver.Chrome):
        self.driver = driver
        self.driver.get(ui_URL)

    @allure.step("Поиск книги по названию {book_title}")
    def search_book_title(self, book_title):
        """Ищет книгу по названию"""
        self.driver.find_element(
            By.CSS_SELECTOR, "[name='phrase']").send_keys(
            book_title, Keys.RETURN)

    @allure.step("Поиск книги по автору {book_author}")
    def search_book_author(self, book_author):
        """Ищет книгу по автору"""
        self.driver.find_element(
            By.CSS_SELECTOR, "[name='phrase']").send_keys(
            book_author, Keys.RETURN)        
