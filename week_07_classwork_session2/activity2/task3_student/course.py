class Course:
    def __init__(self, name, code):
        self.course_name = name
        self.course_code = code

    def __str__(self):
        return f"{self.course_name} ({self.course_code})"

# define the __repr__ method
