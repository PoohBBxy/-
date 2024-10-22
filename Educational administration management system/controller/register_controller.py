from model.login_model import LoginModel
from view.register_view import RegisterView


class RegisterController:
    def __init__(self):
        self.login_model = LoginModel()
        self.register_view = RegisterView()

    def register(self):
        """
        处理用户注册，确保注册的用户信息有效
        """
        username, password, user_type = self.register_view.get_registration_input()

        # 检查用户名是否存在
        if not self.login_model.validate_login(username, password):
            self.login_model.register_user(username, password, user_type)
            self.register_view.show_registration_success(username)
        else:
            self.register_view.show_registration_error(username)
