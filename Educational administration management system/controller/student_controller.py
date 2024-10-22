from model.student_model import StudentModel
from view.student_view import StudentView


class StudentController:
    def __init__(self):
        self.student_model = StudentModel()
        self.student_view = StudentView()

    def perform_main_operation(self, student_id):
        """
        学生操作菜单：查看学生信息、成绩等
        :param student_id: 当前学生ID
        """
        student_info = self.student_model.get_student_info(student_id)
        self.student_view.display_student_info(student_info)

        scores = self.student_model.get_student_scores(student_id)
        self.student_view.display_student_scores(scores)
