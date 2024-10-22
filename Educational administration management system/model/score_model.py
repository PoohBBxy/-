from config.db_config import get_connection


class ScoreModel:
    def __init__(self):
        self.connection = get_connection()

    def get_student_scores(self, student_id):
        """
        根据学生ID获取学生成绩信息
        :param student_id: 学生的ID
        :return: 学生成绩列表
        """
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM scores WHERE student_id = %s"
            cursor.execute(sql, (student_id,))
            return cursor.fetchall()

    def set_student_score(self, student_id, course_id, score):
        """
        更新学生的成绩
        :param student_id: 学生ID
        :param course_id: 课程ID
        :param score: 成绩
        :return: None
        """
        with self.connection.cursor() as cursor:
            sql = "INSERT INTO scores (student_id, course_id, score) VALUES (%s, %s, %s) " \
                  "ON DUPLICATE KEY UPDATE score=%s"
            cursor.execute(sql, (student_id, course_id, score, score))
            self.connection.commit()

    def is_valid_score(self, score):
        """
        验证成绩是否在合理范围内 (0-MaxSize)
        :param score: 输入的成绩
        :return: True 如果成绩有效, 否则 False
        """
        maxsize = 100
        try:
            score = float(score)
            if 0 <= score <= maxsize:
                return True
            else:
                return False
        except ValueError:
            return False
