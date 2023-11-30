SELECT email
FROM Student INNER JOIN Course
ON Student.stu_subject_code = Course.course_code
WHERE course_level = 3;