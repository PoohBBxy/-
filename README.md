
# 教务管理系统

# 目录结构

```
.
├── controller               # 控制器目录，处理用户操作逻辑
│   ├── login_controller.py          # 登录功能控制器
│   ├── student_controller.py        # 学生功能控制器
│   ├── teacher_controller.py        # 教师功能控制器
│   ├── academic_affairs_controller.py # 教务管理功能控制器
│   ├── register_controller.py       # 注册功能控制器
├── model                    # 数据模型目录，负责与数据库的交互
│   ├── student_model.py      # 学生模型
│   ├── teacher_model.py      # 教师模型
│   ├── course_model.py       # 课程模型
│   ├── exam_arrangement_model.py # 考试安排模型
│   ├── score_model.py        # 成绩模型
│   ├── login_model.py        # 登录模型
├── view                     # 视图目录，负责展示和输入界面
│   ├── login_view.py         # 登录视图
│   ├── student_view.py       # 学生视图
│   ├── teacher_view.py       # 教师视图
│   ├── academic_affairs_view.py # 教务视图
│   ├── register_view.py      # 注册视图
├── config                   # 配置文件
│   ├── db_config.py          # 数据库配置
└── main.py                  # 项目入口文件
```

## 项目简介

本系统提供以下功能：

- 用户登录与注册
- 学生信息查询与成绩管理
- 教师课程与成绩录入
- 教务人员管理课程和学生
- 使用 `pymysql` 模块与 MySQL 数据库进行交互

系统分为 MVC 架构，其中 `controller` 负责用户操作逻辑，`model` 负责数据库交互，`view` 负责用户界面展示。

## 如何运行

1. 安装所需的依赖：
   ```bash
   pip install pymysql
   ```

2. 确保 MySQL 数据库已安装并启动，且配置正确的数据库连接信息。

3. 运行系统：
   ```bash
   python main.py
   ```

## 数据库配置

数据库的连接信息存储在 `config/db_config.py` 中，根据实际环境修改以下配置项：

```python
import pymysql

def get_connection():
    return pymysql.connect(
        host="localhost",         # 数据库主机地址
        user="root",              # 数据库用户名
        password="Password123!",  # 数据库密码
        database="academic_management",  # 数据库名称
        charset="utf8mb4",
        cursorclass=pymysql.cursors.DictCursor
    )
```

### 数据库表结构

在 MySQL 数据库中，创建以下表：

```sql
CREATE DATABASE academic_management;

USE academic_management;

CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,
    username VARCHAR(50) NOT NULL,
    password VARCHAR(50) NOT NULL,
    user_type ENUM('student', 'teacher', 'admin') NOT NULL
);

CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    grade INT,
    major VARCHAR(100)
);

CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,
    name VARCHAR(50),
    title VARCHAR(50)
);

CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,
    course_name VARCHAR(100),
    credits INT,
    teacher_id INT,
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id)
);

CREATE TABLE scores (
    student_id INT,
    course_id INT,
    score DECIMAL(5, 2),
    PRIMARY KEY (student_id, course_id),
    FOREIGN KEY (student_id) REFERENCES students(student_id),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);

CREATE TABLE exam_arrangements (
    exam_id INT AUTO_INCREMENT PRIMARY KEY,
    course_id INT,
    exam_time DATETIME,
    exam_location VARCHAR(100),
    FOREIGN KEY (course_id) REFERENCES courses(course_id)
);
```

## 系统功能

### 1. 登录与注册

- 用户通过 `login_controller.py` 进行登录或注册。
- 支持三类用户登录：学生（student）、教师（teacher）和管理员（admin）。

### 2. 学生功能

- 查询个人信息和成绩。
- 实现方式在 `student_controller.py` 和 `student_model.py` 中定义。

### 3. 教师功能

- 查看课程信息，录入学生成绩。
- 实现方式在 `teacher_controller.py` 和 `teacher_model.py` 中定义。

### 4. 教务功能

- 管理课程、学生和教师信息。
- 实现方式在 `academic_affairs_controller.py` 和 `course_model.py` 中定义。

```
