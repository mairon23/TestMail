from data.test_data import UserData
from pages.base import BasePageObject
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException


class LoginPage(BasePageObject):
    """Класс, предоставляющий методы для работы со страницей авторизации."""

    login_button = (By.XPATH, "//button[@data-testid='enter-mail-primary']")
    login_input = (By.XPATH, "//input[@placeholder='Имя аккаунта']")
    enter_password_button = (By.XPATH, "//button[@data-test-id='next-button']")
    password_input = (By.XPATH, "//input[@name='password']")
    enter_button = (By.XPATH, "//button[@data-test-id='submit-button']")
    frame = (By.XPATH, "//iframe[@class='ag-popup__frame__layout__iframe']")

    def click_enter(self) -> None:
        """Кликает на кнопку войти."""
        self.click(self.login_button)

    def do_login(self, login: str) -> None:
        """Вводит логин."""
        self.driver.switch_to.frame(self.wait_located(self.frame))
        self.wait_located(self.login_input).send_keys(login)
        self.click(self.enter_password_button)

    def do_password(self, password: str) -> None:
        """Вводит пароль."""
        self.element_clickable(self.password_input).send_keys(password)
        self.click(self.enter_button)


class IncomingMessagePage(BasePageObject):
    """Класс, предоставляющий методы для работы со страницей 'Входищие сообщения'."""

    message_subject_locator = (By.XPATH, "//span[text()='Автотест']")
    self_mail_tab = (By.XPATH, "//span[text()='Письма себе']")
    number_messages_from_one_user = (By.XPATH, "//div[@class='llc__content']/div[3]//span/span")
    check = (By.XPATH, "//span[@class='ll-sj__normal']//ancestor::div[@class='llc__container']//span["
                       "@class='badge__text']")

    def get_number_message(self) -> int:
        """Возвращает количество сообщений."""
        number_of_messages = 0
        initial_number_of_message = len(self.find_elements(self.message_subject_locator))
        self.is_clickable(self.self_mail_tab)
        try:
            if self.wait_located(self.check).is_displayed():
                for elem in self.find_elements(self.check):
                    number_of_messages = number_of_messages + int(elem.text)
        except NoSuchElementException:
            pass
        return int(number_of_messages) - int(initial_number_of_message) + 1 + \
               len(self.find_elements(self.message_subject_locator))


class SendMessagePage(IncomingMessagePage):
    """Класс, предоставляющий методы для работы со страницей отправки сообщений."""

    reply_button = (By.XPATH, "//span[text()='Ответить']")
    topic_field = (By.XPATH, "//input[@name='Subject']")
    send_button = (By.XPATH, "//button[@data-test-id='send']")
    text_message = (By.XPATH, "//div[@role='textbox']/div")
    message_mail_sent = (By.XPATH, "//a[@class='layer__link']")

    def send_message(self, message_count: int) -> None:
        """
        Отправляет сообщение.

        :param message_count: Количество сообщений.
        """
        self.wait_located(self.message_subject_locator).click()
        self.wait_located(self.reply_button).click()
        self.wait_located(self.text_message).send_keys(message_count)
        self.wait_located(self.topic_field).clear()
        self.wait_located(self.topic_field).send_keys(UserData.message_topic)
        self.wait_located(self.send_button).click()

    def check_mail_sent(self) -> str:
        """Проверка отправки сообщения."""
        if self.wait_located(self.message_mail_sent).is_displayed():
            return self.wait_located(self.message_mail_sent).text
