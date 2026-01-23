-- Student table
CREATE TABLE IF NOT EXISTS student (
    student_id INTEGER PRIMARY KEY,
    level INTEGER,
    target TEXT
);

-- Course table
CREATE TABLE IF NOT EXISTS course (
    course_id INTEGER PRIMARY KEY,
    course_name TEXT,
    difficulty INTEGER
);

-- Prerequisite relationship (DAG)
CREATE TABLE IF NOT EXISTS prerequisite (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    course_id INTEGER,
    pre_course_id INTEGER,
    FOREIGN KEY(course_id) REFERENCES course(course_id),
    FOREIGN KEY(pre_course_id) REFERENCES course(course_id)
);

-- Student learning record
CREATE TABLE IF NOT EXISTS student_course (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    student_id INTEGER,
    course_id INTEGER,
    status TEXT,
    score INTEGER,
    FOREIGN KEY(student_id) REFERENCES student(student_id),
    FOREIGN KEY(course_id) REFERENCES course(course_id)
);

-- Learning resources
CREATE TABLE IF NOT EXISTS resource (
    resource_id INTEGER PRIMARY KEY,
    course_id INTEGER,
    resource_type TEXT,
    url TEXT,
    difficulty INTEGER,
    FOREIGN KEY(course_id) REFERENCES course(course_id)
);
