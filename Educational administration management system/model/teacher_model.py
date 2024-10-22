from config.db_config import get_connection


class TeacherModel:
    def __init__(self):
        self.connection = get_connection()

    def get_teacher_info(self, teacher_id):
        """
        根据教师ID获取教师信息
        :param teacher_id: 教师的ID
        :return: 教师的详细信息
        """
        with self.connection.cursor() as cursor:
            sql = "SELECT * FROM teachers WHERE teacher_id = %s"
            cursor.execute(sql, (teacher_id,))
            return cursor.fetchone()

    def set_teacher_info(self, teacher_id, name, title):
        """
        更新教师信息
        :param teacher_id: 教师ID
        :param name: 教师姓名
        :param title: 教师职称
        :return: None
        """
        with self.connection.cursor() as cursor:
            sql = "UPDATE teachers SET name=%s, title=%s WHERE teacher_id=%s"
            cursor.execute(sql, (name, title, teacher_id))
            self.connection.commit()
