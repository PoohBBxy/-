from model.login_model import LoginModel
from view.login_view import LoginView
from controller.student_controller import StudentController
from controller.teacher_controller import TeacherController
from controller.academic_affairs_controller import AcademicAffairsController
from controller.register_controller import RegisterController


class LoginController:
    def __init__(self):
        self.login_model = LoginModel()
        self.login_view = LoginView()
        self.register_controller = RegisterController()

    def login(self):
        """
        处理用户的登录请求或注册请求
        """
        while True:
            choice = self.login_view.show_login_menu()

            if choice == '1':  # 登录
                username, password = self.login_view.get_login_input()
                user_info = self.login_model.validate_login(username, password)

                if user_info:
                    self.login_view.show_login_success(username)
                    user_type = user_info['user_type']
                    self.handle_user_menu(user_type, username)
                else:
                    self.login_view.show_login_error()

            elif choice == '2':  # 注册
                self.register_controller.register()

            elif choice == '3':  # 退出系统
                print("系统已退出。")
                break

    def handle_user_menu(self, user_type, username):
        """
        根据用户类型引导到相应的控制器进行操作
        :param user_type: 用户类型 (student/teacher/admin)
        :param username: 当前登录用户名
        """
        if user_type == 'student':
            controller = StudentController()
        elif user_type == 'teacher':
            controller = TeacherController()
        elif user_type == 'admin':
            controller = AcademicAffairsController()
        else:
            print("未知用户类型，无法继续操作。")
            return

        # 循环处理用户操作
        while True:
            user_choice = self.login_view.show_user_menu(user_type)
            if user_choice == '1':
                controller.perform_main_operation(username)  # 执行主要功能
            elif user_choice == '2':
                print(f"{username} 已成功退出登录。")
                break
            else:
                print("无效选择，请重试。")
