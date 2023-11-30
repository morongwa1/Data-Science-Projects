DROP TABLE IF EXISTS Student;

CREATE TABLE Student (
STU_NUM CHAR(6),
STU_SNAME VARCHAR(15),
STU_FNAME VARCHAR(15),
STU_INITIAL CHAR(1),
STU_STARTDATE DATE,
COURSE_CODE CHAR(3),
PROJ_NUM INT(2),
PRIMARY KEY (STU_NUM)
);


INSERT INTO Student 
VALUES
('01', 'Snow', 'Jon', 'E', '2014-04-05', '201', 6),
('02', 'Stark', 'Arya', 'C', '2017-07-012', '305',11),
('03', 'Lannister', 'Jamie', 'C', '2012-09-05', '101', 2),
('04', 'Lannister', 'Cercie', 'J', '2012-09-05', '101', 2),
('05', 'Greyjoy', 'Theon', 'I', '2015-12-09', '402', 14),
('06', 'Tyrell', 'Margaery', 'Y', '2017-07-12', '305', 10),
('07', 'Baratheon', 'Tommen', 'R', '2019-06-13', '201', 5)


