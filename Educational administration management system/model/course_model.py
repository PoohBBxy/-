from config.db_config import get_connection


class CourseModel:
    def __init__(self):
        self.connection = get_connection()

    def get_course_info(self, course_id):
        """
        根据课程ID获取课程信息
        :param course_id: 课程的ID
        :return: 课程的详细信息
        """
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM courses WHERE course_id = %s"
            cursor.execute(sql, (course_id,))
            return cursor.fetchone()

    def set_course_info(self, course_id, course_name, credits, teacher_id):
        """
        更新课程信息
        :param course_id: 课程ID
        :param course_name: 课程名称
        :param credits: 课程学分
        :param teacher_id: 教师ID
        :return: None
        """
        with self.connection.cursor() as cursor:
            sql = "UPDATE courses SET course_name=%s, credits=%s, teacher_id=%s WHERE course_id=%s"
            cursor.execute(sql, (course_name, credits, teacher_id, course_id))
            self.connection.commit()

    def get_all_courses(self):
        """
        获取所有课程的信息
        :return: 所有课程的列表
        """
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM courses"
            cursor.execute(sql)
            return cursor.fetchall()
