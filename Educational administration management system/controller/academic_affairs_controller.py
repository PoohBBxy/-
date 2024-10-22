from model.course_model import CourseModel
from view.academic_affairs_view import AcademicAffairsView


class AcademicAffairsController:
    def __init__(self):
        self.course_model = CourseModel()
        self.academic_view = AcademicAffairsView()

    def perform_main_operation(self, admin_id):
        """
        教务处操作：管理课程、学生、教师
        :param admin_id: 当前管理员ID
        """
        courses = self.course_model.get_all_courses()
        self.academic_view.display_courses(courses)

