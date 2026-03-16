class Book:
    def __init__(self, title, author, year, edition):
        self.title = title
        self.author = author
        self.year = year
        self.edition = edition

    def __str__(self):
        return f"{self.title} by {self.author} ({self.year}) - {self.edition} edition"


# write setter for year and update the __init__ method


# define the __repr__ method


