SELECT first_name, course_name
FROM Student INNER JOIN Course
ON Student.stu_subject_code = Course.course_code
WHERE mark >= 70;