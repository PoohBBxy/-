from config.db_config import get_connection


class LoginModel:
    def __init__(self):
        self.connection = get_connection()

    def validate_login(self, username, password):
        """
        验证用户的登录信息。
        :param username: 用户名
        :param password: 密码
        :return: 用户信息字典（包含用户名和类型）或 None
        """
        with self.connection.cursor() as cursor:
            sql = "SELECT username, user_type FROM users WHERE username = %s AND password = %s"
            cursor.execute(sql, (username, password))
            return cursor.fetchone()

    def register_user(self, username, password, user_type):
        """
        注册新用户
        :param username: 用户名
        :param password: 密码
        :param user_type: 用户类型（student, teacher, admin）
        :return: None
        """
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO users (username, password, user_type) VALUES (%s, %s, %s)"
            cursor.execute(sql, (username, password, user_type))
            self.connection.commit()
