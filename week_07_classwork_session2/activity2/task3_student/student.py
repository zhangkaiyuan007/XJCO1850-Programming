# write code to import the course and grade modules


# define a Student class with the following fields:
# (1) name - the name of a student
# (2) student_id - an unique student id
# (3) grades - a list of Grade instances, initialised to an empty list




# the Student class also has the following methods:
# (1) add_grade(grade) - adds a Grade instance to the student record, i.e., add to the grades list
# (2) __str__: returning student's name, id, and list of courses with grades
#    Example output
#    Student: Alice Johnson (ID: 12345)
#    Grades:
#    - Math 101 (MATH101): 95
#    - History 201 (HIST201): 88









# once completed, 
# (1) create two instances of Course, put any course you like, e.g., course1 = Course("Programming", "COMP1850")
# (2) create two instances of Grade for the courses you just created with a score for each course, e.g., grade1 = Grade(course1, 95)
# (3) create an instance of Student with your details., e.g., student = Student("Alice Johnson", '12345')
# (4) add the grades to the Student instance, e.g., student.add_grade(grade1)
# (5) print(student)





# extended task - creating instances of Course and Grade from methods inside Student
# define another method called load_grade(filename) that load grades from a text file
# and then add grade data from the text file into the field grade
# once done, call that method and the print(student)
