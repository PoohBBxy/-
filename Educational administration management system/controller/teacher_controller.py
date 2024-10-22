from model.teacher_model import TeacherModel
from model.score_model import ScoreModel
from view.teacher_view import TeacherView

class TeacherController:
    def __init__(self):
        self.teacher_model = TeacherModel()
        self.score_model = ScoreModel()
        self.teacher_view = TeacherView()

    def perform_main_operation(self, teacher_id):
        """
        教师操作：查看课程、录入成绩
        :param teacher_id: 当前教师ID
        """
        teacher_info = self.teacher_model.get_teacher_info(teacher_id)
        self.teacher_view.display_teacher_info(teacher_info)

        student_id, course_id, score = self.teacher_view.get_input_score()

        # 检查输入数据的有效性
        if self.score_model.is_valid_score(score):
            self.score_model.set_student_score(student_id, course_id, score)
            self.teacher_view.display_input_success()
        else:
            print("成绩输入无效，请重新尝试。")
