# 全是BUG！！！！！准备重写了

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

在 MySQL 数据库中，创建以下表：

```sql
-- 创建数据库
CREATE DATABASE academic_management;

-- 使用数据库
USE academic_management;

-- 创建用户表
CREATE TABLE users (
    user_id INT AUTO_INCREMENT PRIMARY KEY,          -- 用户ID，自动递增
    username VARCHAR(50) NOT NULL,                   -- 用户名
    password VARCHAR(50) NOT NULL,                   -- 密码
    user_type ENUM('student', 'teacher', 'admin') NOT NULL  -- 用户类型：学生、教师或管理员
);

-- 创建学生表
CREATE TABLE students (
    student_id INT AUTO_INCREMENT PRIMARY KEY,       -- 学生ID，自动递增
    name VARCHAR(50),                                -- 学生姓名
    grade INT,                                       -- 年级
    major VARCHAR(100)                               -- 专业
);

-- 创建教师表
CREATE TABLE teachers (
    teacher_id INT AUTO_INCREMENT PRIMARY KEY,       -- 教师ID，自动递增
    name VARCHAR(50),                                -- 教师姓名
    title VARCHAR(50)                                -- 教师职称
);

-- 创建课程表
CREATE TABLE courses (
    course_id INT AUTO_INCREMENT PRIMARY KEY,        -- 课程ID，自动递增
    course_name VARCHAR(100),                        -- 课程名称
    credits INT,                                     -- 学分
    teacher_id INT,                                  -- 任课教师ID，外键引用教师表
    FOREIGN KEY (teacher_id) REFERENCES teachers(teacher_id) -- 设置外键，关联教师表
);

-- 创建成绩表
CREATE TABLE scores (
    student_id INT,                                  -- 学生ID，外键引用学生表
    course_id INT,                                   -- 课程ID，外键引用课程表
    score DECIMAL(5, 2),                             -- 成绩
    PRIMARY KEY (student_id, course_id),             -- 联合主键，确保学生和课程的唯一性
    FOREIGN KEY (student_id) REFERENCES students(student_id), -- 设置外键，关联学生表
    FOREIGN KEY (course_id) REFERENCES courses(course_id)      -- 设置外键，关联课程表
);

-- 创建考试安排表
CREATE TABLE exam_arrangements (
    exam_id INT AUTO_INCREMENT PRIMARY KEY,          -- 考试ID，自动递增
    course_id INT,                                   -- 课程ID，外键引用课程表
    exam_time DATETIME,                              -- 考试时间
    exam_location VARCHAR(100),                      -- 考试地点
    FOREIGN KEY (course_id) REFERENCES courses(course_id)      -- 设置外键，关联课程表
);

```
### 数据库示例数据
#### users 示例数据
```
| user_id | username | password | user_type | logged_in |
|---------|----------|----------|-----------|-----------|
| 1       | admin    | 123456   | admin     | 0         |
| 2       | student  | 123456   | student   | 0         |

```
#### students 示例数据
```
| student_id | name      | grade | major         |
|------------|-----------|-------|---------------|
| 1          | 张三       | 3     | 计算机科学与技术 |
| 2          | 李四       | 2     | 大数据技术与应用 |

```
#### teachers 示例数据
```
| teacher_id | name       | title        |
|------------|------------|--------------|
| 1          | 李明        | 教授          |
| 2          | 刘刚        | 讲师          |

```
#### courses 示例数据
```
| course_id | course_name  | credits | teacher_id |
|-----------|--------------|---------|------------|
| 1         | 数据科学      | 4       | 1          |
| 2         | 软件工程      | 3       | 2          |

```
#### scores 示例数据
```
| student_id | course_id | score |
|------------|-----------|-------|
| 1          | 1         | 85.50 |
| 2          | 2         | 78.00 |

```
#### exam_arrangements 示例数据
```
| exam_id | course_id | exam_time         | exam_location |
|---------|-----------|-------------------|---------------|
| 1       | 1         | 2024-12-15 09:00  | 教8 101       |
| 2       | 2         | 2024-12-18 13:00  | 教10 202      |
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
