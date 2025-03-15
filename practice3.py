class Book:
    def __init__(self, title, author, year):
        self.title = title
        self.author = author
        self.year = year

    def __str__(self):
        return f"Title: [{self.title}], Author: [{self.author}], Publication Year: [{self.year}]"

class Library:
    def __init__(self):
        self.books = []

    def add_book(self, book):
        self.books.append(book)

    def add_books(self, books):
        for book in books:
            self.add_book(book)


    def show_books(self):
        print("Our library contains the following books:")
        for book in self.books:
            print(f"- Title: [{book.title}], Author: [{book.author}], Publication Year: [{book.year}]")

    def find_book(self, title):
        for book in self.books:
            if book.title == title:
                print("Book in library:")
                print(book)
                return
        print("No such book exists in the library")


books = [
    Book("The Midnight Library", "Matt Haig", 2020),
    Book("Where the Crawdads Sing", "Delia Owens", 2018),
    Book("The Silent Patient", "Alex Michaelides", 2019),
    Book("Project Hail Mary", "Andy Weir", 2021),
    Book("The Night Watchman", "Louise Erdrich", 2020),
    Book("The Paper Palace", "Miranda Cowley Heller", 2021),
    Book("It Ends With Us", "Colleen Hoover", 2016),
    Book("The Paris Library", "Janet Skeslien Charles", 2021),
    Book("The Four Winds", "Kristin Hannah", 2021),
    Book("A Man Called Ove", "Fredrik Backman", 2012),
]


library = Library()

library.add_books(books)


library.show_books()



library.find_book("The Silent Patient")
