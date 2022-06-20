from dataclasses import dataclass


@dataclass
class Routes:
    main_page: str = "https://mail.ru/"


@dataclass
class UserData:
    login: str = "login"
    password: str = "password"
    message_topic: str = "Фамилия И.О."


@dataclass
class SendMessage:
    message_sent: str = "Письмо отправлено"
