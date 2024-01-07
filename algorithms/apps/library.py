class Book:
    """
    An instance of book in a Library
    """

    id_cnt = 1

    def __init__(self, title, author, content, genre):
        self.title = title
        self.content = content
        self.author = author
        self.genre = genre
        self.book_id = self.id_cnt
        Book.id_cnt +=1

    def display(self):
        """
        Displays information about the Book
        """
        print(f'ID: {self.book_id}')
        print(f'Title: {self.title}')
        print(f'Author: {self.author}')
        print(f'Genre: {self.genre}')


class Library:
    """
    A Library that stores the books, authors and genre
    """
    
    def __init__(self):
        self.books = {}
        self.recently_read = {}
        self.genre = {}
        self.author = {}

    def add_book(self, book):
        """
        Adds a Book to the Library
        :type book: Book
        """
        self.books[book.book_id] = book

        if book.genre not in self.genre:
            self.genre[book.genre] = []
        self.genre[book.genre].append(book)

        if book.autor not in self.author:
            self.author[book.author] = []
        self.author[book.autor].append(book)

        print(f'{book.title} has been added to Library successfully')

    def recently_read_book(self, book):
        """
        Marks a book as recently read
        :type book: Book
        """
        self.recently_read[book.book_id] = book
        print(f'{book.title} is your recently read book')
    
    def display_genre(self):
        """
        Display books grouped by Genre
        """
        for genre, books in self.genre.items():
            print(f'{genre} Genre:')
            for book in books:  
                book.display()
        
    def display_by_author(self):
        """
        Display books grouped by Authors
        """
        for author, books in self.author.items():
            print(f'{author} Author:')
            for book in books:
                book.display()
    
    def books_by_author(self, author):
        """
        Display books of specific author
        :type author: str
        """
        if author in self.author:
            print(f'books by {author}:')
            for book in self.author[author]:
                book.display()
        print(f'No books related to {author}')
