class LoginView:
    def show_login_menu(self):
        """
        显示登录菜单，允许选择登录、注册或退出
        :return: 选择的选项
        """
        print("1. 登录")
        print("2. 注册")
        print("3. 退出系统")
        choice = input("请选择操作：")
        return choice

    def get_login_input(self):
        username = input("请输入用户名：")
        password = input("请输入密码：")
        return username, password

    def show_login_success(self, username):
        print(f"欢迎 {username} 登录成功！")

    def show_login_error(self):
        print("登录失败，用户名或密码错误。")

    def show_user_menu(self, user_type):
        """
        显示用户登录后的功能菜单，依据用户类型显示不同功能。
        :param user_type: 用户类型
        :return: 用户选择的功能
        """
        print("\n功能菜单:")
        if user_type == 'student':
            print("1. 查询课程/成绩等信息")
        elif user_type == 'teacher':
            print("1. 查询课程/学生信息，录入成绩")
        elif user_type == 'admin':
            print("1. 管理学生/教师/课程信息")

        print("2. 退出登录")
        return input("请选择操作：")
