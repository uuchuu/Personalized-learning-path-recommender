CREATE TABLE majors (
    major_id INT PRIMARY KEY,
    major_name VARCHAR(50)
);
-- 专业表
CREATE TABLE courses (
    course_id INT PRIMARY KEY,
    course_name VARCHAR(100),
    major_id INT,
    difficulty INT,
    course_type VARCHAR(50),
    credit FLOAT,
    FOREIGN KEY (major_id) REFERENCES majors(major_id)
);
-- 课程细节
CREATE TABLE course_prerequisite (
    id INT PRIMARY KEY,
    course_id INT,
    prereq_course_id INT,
    FOREIGN KEY (course_id) REFERENCES courses(course_id),
    FOREIGN KEY (prereq_course_id) REFERENCES courses(course_id)
);
-- 先修关系
