class StudentView:
    def display_student_info(self, student_info):
        print("学生信息：", student_info)

    def display_student_scores(self, scores):
        print("学生成绩：")
        for score in scores:
            print(f"课程ID: {score['course_id']}, 成绩: {score['score']}")
