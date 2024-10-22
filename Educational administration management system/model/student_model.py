from config.db_config import get_connection


class StudentModel:
    def __init__(self):
        self.connection = get_connection()

    def get_student_info(self, student_id):
        """
        根据学生ID获取学生信息
        :param student_id: 学生的ID
        :return: 学生的详细信息
        """
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM students WHERE student_id = %s"
            cursor.execute(sql, (student_id,))
            return cursor.fetchone()

    def set_student_info(self, student_id, name, grade, major):
        """
        更新学生信息
        :param student_id: 学生ID
        :param name: 学生姓名
        :param grade: 学生年级
        :param major: 学生专业
        :return: None
        """
        with self.connection.cursor() as cursor:
            sql = "UPDATE students SET name=%s, grade=%s, major=%s WHERE student_id=%s"
            cursor.execute(sql, (name, grade, major, student_id))
            self.connection.commit()

    def get_student_scores(self, student_id):
        """
        根据学生ID获取该学生的所有成绩
        :param student_id: 学生ID
        :return: 学生成绩的列表
        """
        with self.connection.cursor() as cursor:
            sql = """
            SELECT courses.course_name, scores.score
            FROM scores
            JOIN courses ON scores.course_id = courses.course_id
            WHERE scores.student_id = %s
            """
            cursor.execute(sql, (student_id,))
            return cursor.fetchall()
