"""Демомодуль для курса"""


class Auth:
    """Авторизация пользователя"""
    is_authed: bool = False

    def login(self):
        """Вход"""
        self.is_authed = True

    def logout(self):
        """Выход"""
        self.is_authed = False


auth_service = Auth()
auth_service.login()  # Пользователь авторизировался
# Auth.login(auth_service)  # Пользователь авторизировался
print(auth_service.is_authed)  # True
auth_service.logout()  # Пользователь вышел
print(auth_service.is_authed)  # False
