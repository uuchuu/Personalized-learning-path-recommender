INSERT INTO course VALUES (1, 'Programming Basics', 1);
INSERT INTO course VALUES (2, 'Data Structures', 2);
INSERT INTO course VALUES (3, 'Database Systems', 3);
INSERT INTO course VALUES (4, 'Machine Learning', 4);

INSERT INTO prerequisite (course_id, pre_course_id) VALUES (2,1);
INSERT INTO prerequisite (course_id, pre_course_id) VALUES (3,2);
INSERT INTO prerequisite (course_id, pre_course_id) VALUES (4,3);
