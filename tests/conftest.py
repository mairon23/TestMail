import pytest
from selenium import webdriver
from pages.mail import LoginPage, IncomingMessagePage
from data.test_data import Routes, UserData


@pytest.fixture
def driver():
    driver = webdriver.Chrome("chromedriver.exe")
    driver.get(Routes.main_page)
    yield driver
    driver.quit()


@pytest.fixture
def authorized_user(driver):
    log_in = LoginPage(driver)
    log_in.click_enter()
    log_in.do_login(UserData.login)
    log_in.do_password(UserData.password)
    return driver


@pytest.fixture
def check_message(authorized_user):
    select = IncomingMessagePage(authorized_user)
    select.get_number_message()
    return driver
