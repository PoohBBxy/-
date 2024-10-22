from config.db_config import get_connection


class ExamArrangementModel:
    def __init__(self):
        self.connection = get_connection()

    def get_exam_arrangement(self, exam_id):
        """
        根据考试ID获取考试安排信息
        :param exam_id: 考试ID
        :return: 考试的详细信息
        """
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM exam_arrangements WHERE exam_id = %s"
            cursor.execute(sql, (exam_id,))
            return cursor.fetchone()

    def set_exam_arrangement(self, exam_id, course_id, exam_time, exam_location):
        """
        更新考试安排信息
        :param exam_id: 考试ID
        :param course_id: 课程ID
        :param exam_time: 考试时间
        :param exam_location: 考试地点
        :return: None
        """
        with self.connection.cursor() as cursor:
            sql = "UPDATE exam_arrangements SET course_id=%s, exam_time=%s, exam_location=%s WHERE exam_id=%s"
            cursor.execute(sql, (course_id, exam_time, exam_location, exam_id))
            self.connection.commit()
