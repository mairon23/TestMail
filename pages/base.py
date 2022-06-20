from typing import List
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException


class BasePageObject(object):
    """Класс, предоставляющий базовые методы для работы с веб-элементами."""

    def __init__(self, driver):
        self.driver = driver

    def wait_located(self, locator: tuple) -> WebElement:
        """
        Ожидает появление элемента на странице и возвращает его.

        :param locator: Кортеж, с методом поиска и локатором элемента.
        """
        return WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))

    def click(self, locator: tuple) -> None:
        """
        Кликает на элемент на странице.

        :param locator: Кортеж, с методом поиска и локатором элемента.
        """
        self.element_clickable(locator).click()

    def find_elements(self, locator: tuple) -> List[WebElement]:
        """
        Возвращает список элементов DOM.

        :param locator: Кортеж, с методом поиска и локатором элемента.
        """
        return WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located(locator))

    def element_clickable(self, locator: tuple) -> WebElement:
        """
        Ожидает кликабельности элемента и возвращает его.

        :param locator: Кортеж, с методом поиска и локатором элемента.
        """
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    def is_clickable(self, locator: tuple) -> bool:
        """
        Проверяет элемент на кликабельность.

        :param locator: Кортеж, с методом поиска и локатором элемента.
        """
        try:
            self.click(locator)
            return True
        except TimeoutException:
            return False
