class RegisterView:
    def get_registration_input(self):
        """
        获取注册信息输入
        :return: 用户名、密码、用户类型
        """
        username = input("请输入新用户名：")
        password = input("请输入密码：")
        user_type = input("请输入用户类型（student/teacher/admin）：")
        return username, password, user_type

    def show_registration_success(self, username):
        """
        显示注册成功信息
        :param username: 成功注册的用户名
        """
        print(f"用户 {username} 注册成功！")

    def show_registration_error(self, username):
        """
        显示注册错误信息
        :param username: 尝试注册的用户名
        """
        print(f"用户名 {username} 已存在，请尝试其他用户名。")
