import datetime

class Book:
    def __init__(self, title, author, id, location):
        self.title = title
        self.author = author
        self.id = id
        self.is_borrowed = False
        self.borrow_time = None
        self.location = location

    def borrow(self):
        if not self.is_borrowed:
            self.is_borrowed = True
            self.borrow_time = datetime.datetime.now()
            return True
        else:
            return False

    def return_book(self):
        if self.is_borrowed:
            self.is_borrowed = False
            self.borrow_time = None
            return True
        else:
            return False

    def info(self):
        return f"name: {self.title}\nauthor: {self.author}\nid: {self.id}\nis borrowed?: {self.is_borrowed}\nborrow time: {self.borrow_time}\nlocation: {self.location}"

class Library:
    def __init__(self):
        self.books = {}

    def add_book(self, title, author, id, location):
        book = Book(title, author, id, location)
        self.books[id] = book

    def get_book_by_id(self, id):
        if id in self.books:
            return self.books[id].info()
        else:
            return "not found"

    def get_books_by_author(self, author):
        books_by_author = [book for book in self.books.values() if book.author == author]
        if books_by_author:
            return "\n".join([book.info() for book in books_by_author])
        else:
            return "not found"
    def get_books_by_title(self, title):
            books_by_title = [book for book in self.books.values() if book.title == title]
            if books_by_title:
                return "\n".join([book.info() for book in books_by_title])
            else:
                return "not found"

def test_library():

    library = Library()


    library.add_book("書名1", "作者1", "編號1", "儲藏位置1")
    library.add_book("書名2", "作者1", "編號2", "儲藏位置2")
    library.add_book("書名3", "作者3", "編號3", "儲藏位置3")

    # 書名
    

    # id
    print(library.get_book_by_id("編號1"))
    print(library.get_book_by_id("編號4"))

    # 作者
    print(library.get_books_by_author("作者1")+"\n")
    print(library.get_books_by_author("作者4"))

test_library()

test_library()
