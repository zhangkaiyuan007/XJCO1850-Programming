class LibraryItem:
    def __init__(self, title, publication_date):
        self.title = title
        self.publication_date = publication_date
        self.is_checked_out = False

    def check_out(self):
        if not self.is_checked_out:
            self.is_checked_out = True
            print(f"{self.title} has been checked out.")
        else:
            print(f"{self.title} is already checked out.")

    def return_item(self):
        if self.is_checked_out:
            self.is_checked_out = False
            print(f"{self.title} has been returned.")
        else:
            print(f"{self.title} is already in the library.")

    def __str__(self):
        return f"{self.title} (Published on {self.publication_date})"


class Book(LibraryItem):
    def __init__(self, title, publication_date, author, num_pages):
        super().__init__(title, publication_date)
        self.author = author
        self.num_pages = num_pages

    def __str__(self):
        return f"Book: {self.title} by {self.author}, {self.num_pages} pages, published on {self.publication_date}"


class Magazine(LibraryItem):
    def __init__(self, title, publication_date, issue_number, volume):
        super().__init__(title, publication_date)
        self.issue_number = issue_number
        self.volume = volume

    def __str__(self):
        return f"Magazine: {self.title}, Volume {self.volume}, Issue {self.issue_number}, published on {self.publication_date}"


class DVD(LibraryItem):
    def __init__(self, title, publication_date, director, duration):
        super().__init__(title, publication_date)
        self.director = director
        self.duration = duration  # Duration in minutes

    def __str__(self):
        return f"DVD: {self.title} directed by {self.director}, {self.duration} min, released on {self.publication_date}"


# Example usage
book = Book("The Great Gatsby", "1925-04-10", "F. Scott Fitzgerald", 218)
magazine = Magazine("National Geographic", "2023-07-01", 7, 2023)
dvd = DVD("Inception", "2010-07-16", "Christopher Nolan", 148)

print(book)
book.check_out()
book.return_item()

print("\n" + str(magazine))
magazine.check_out()
magazine.return_item()

print("\n" + str(dvd))
dvd.check_out()
dvd.return_item()
