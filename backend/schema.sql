-- 学生表
CREATE TABLE student (
    student_id INTEGER PRIMARY KEY,
    name TEXT,
    level INTEGER,
    target TEXT
);

-- 课程表
CREATE TABLE course (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    difficulty INTEGER,
    credit INTEGER
);

-- 课程先修关系表（有向图）
CREATE TABLE prerequisite (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER,
    pre_course_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES course(course_id),
    FOREIGN KEY(pre_course_id) REFERENCES course(course_id)
);

-- 学生已修课程表
CREATE TABLE student_course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    status TEXT,
    score REAL,
    FOREIGN KEY(student_id) REFERENCES student(student_id),
    FOREIGN KEY(course_id) REFERENCES course(course_id)
);

-- 学习资源表
CREATE TABLE resource (
    resource_id INTEGER PRIMARY KEY,
    course_id INTEGER,
    type TEXT,
    title TEXT,
    url TEXT,
    difficulty INTEGER,
    FOREIGN KEY(course_id) REFERENCES course(course_id)
);
