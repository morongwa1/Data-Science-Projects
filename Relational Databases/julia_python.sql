SELECT mark
FROM Student INNER JOIN Course
ON Student.stu_subject_code = Course.course_code
WHERE teacher_name = 'Julia Python';