import pymysql


def get_connection():
    """
    获取与数据库的连接
    :return: 数据库连接对象
    """
    return pymysql.connect(
        host="localhost",  # 数据库主机地址
        user="root",  # 数据库用户名
        password="Password123!",  # 数据库密码
        database="academic_management",  # 数据库名称
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
