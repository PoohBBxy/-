class TeacherView:
    def display_teacher_info(self, teacher_info):
        print("教师信息：", teacher_info)

    def get_input_score(self):
        student_id = input("输入学生ID：")
        course_id = input("输入课程ID：")
        score = input("输入成绩：")
        return student_id, course_id, score

    def display_input_success(self):
        print("成绩录入成功！")
