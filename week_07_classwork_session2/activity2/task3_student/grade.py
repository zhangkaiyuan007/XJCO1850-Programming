# write code to import course

class Grade:
    def __init__(self, course, score):
        self.course = course
        self.set_score(score)

    def set_score(self, score):
        if score < 0 or score > 100:
            raise ValueError("Invalid score, must be between 0 and 100 inclusive")
        self.score = score

    def __str__(self):
        return f"{self.course}: {self.score}"


# define the __repr__ method
