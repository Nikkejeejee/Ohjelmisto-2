class Publication:
    def __init__(self, books, magazines):
        self.books = books
        self.magazines = magazines

    def print_information(self):
        print("Book "
              f"name: {self.books.name}\n"
              f"Author: {self.books.author}\n"
              f"Page: {self.books.page} pages")

        print("\nMagazine "
              f"name: {self.magazines.name}\n"
              f"Chief Editor: {self.magazines.chief_editor}")


class Book:
    def __init__(self, name, author, page):
        self.name = name
        self.author = author
        self.page = page


class Magazine:
    def __init__(self, name, chief_editor):
        self.name = name
        self.chief_editor = chief_editor


book = Book(name="Compartment No. 6", author="Rosa Likson", page=192)
magazine = Magazine(name="Donald Duck", chief_editor="Aki Hyyppä")
publication = Publication(book, magazine)
publication.print_information()
