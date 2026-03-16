class Movie:
    def __init__(self, title, director, year, genre, duration):
        self.title = title
        self.director = director
        self.year = year
        self.genre = genre
        self.duration = duration

# Define the __str__ and __repr__ in the following format:
# (1) __str__: Inception (2010), directed by Christopher Nolan, Sci-Fi, 148 mins
# (2) __repr__: Movie(title='Inception', director='Christopher Nolan', year=2010, genre='Sci-Fi', duration=148)
