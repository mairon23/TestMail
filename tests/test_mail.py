from data.test_data import SendMessage
from pages.mail import SendMessagePage
from pages.mail import IncomingMessagePage
import allure


@allure.title("тест-mail")
@allure.severity("normal")
def test_mail(authorized_user):
    send_message = SendMessagePage(authorized_user)
    incoming_message = IncomingMessagePage(authorized_user)
    send_message.send_message(incoming_message.get_number_message())
    assert send_message.check_mail_sent() == SendMessage.message_sent
