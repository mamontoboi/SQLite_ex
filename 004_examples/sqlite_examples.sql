CREATE TABLE students_list (
    student_id INTEGER NOT NULL PRIMARY KEY AUTOINCREMENT,
    first_name TEXT NOT NULL,
    last_name TEXT NOT NULL,
    course TEXT NOT NULL,
    lessons INTEGER NOT NULL );
    
    
ALTER TABLE students_list
ADD COLUMN age INTEGER;

ALTER TABLE students_list
RENAME TO students;

INSERT INTO students ( first_name, last_name, course, lessons, age )
VALUES ( 'Rachel', 'Green', 'C#', 40, 26 );

SELECT student_id, first_name, last_name, course, lessons, age
FROM students;

SELECT *
FROM students;

UPDATE students
SET course = 'Python'
WHERE first_name = 'Rachel';

SELECT *
FROM students;

DELETE FROM students
WHERE first_name = 'Rachel';

SELECT *
FROM students;
