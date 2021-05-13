class Book:

    def __init__(self, title: str, price: float, number: int= 0):
        self.title = title
        self.price = price
        self.number = number


    def __repr__(self):
        return f'<Title: {self.title} , Price: {self.price}>'



class BookStore:
    book_cnt : int = 0
    books : list = []

    def __init__(self, book: Book):
        self.book = book

    def __call__(self):
        print('hello world!')


    def __repr__(self):

     return f'Book Title: {self.book.title}, Price: {self.book.price}, Stock in Store: {self.book.number}'

    @classmethod
    def add_stock(cls, book: Book):
        cls.books.append(book)
        cls.book_cnt = cls.book_cnt + book.number

        return cls.book_cnt


book1 = Book('green mile', 1100.25, 0)
book2 = Book('1984', 120, 10)
book3 = Book('little prince', 75, 5)
print(book2)
store1 = BookStore(book1)
store1.add_stock(book3)
store1.add_stock(book2)
store1.add_stock(book1)
print(BookStore.book_cnt)
book4 = Book('python learning', 12000, 4)
print(*BookStore.books)
store1.add_stock(book4)
print(BookStore.book_cnt)
print(*BookStore.books)
store1()


