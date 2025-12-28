class Student:
    def __init__(self, id, name, email): 
        self.id = id
        self.name = name
        self.email = email

    def print_details(self):
        return 'Id: {}, Name: {}, Email:{}'.format(self.id, self.name, self.email)


student_1 = Student("xnct0258", "John Smith", "johnsmith@leeds.ac.uk")
print(student_1.print_details())
student_2 = Student("jytbuwqr", "Varia Costantine", "v.constantine@leeds.ac.uk")
print(student_2.print_details())
