#Data Abstraction and Encapsulation
#Library Management System

class library:
    def __init__(self, books):
        self.books=books

    def list_books(self):
        print('Available Books')
        for book in self.books:
            print(book)

    def borrow_book(self, borrow_book):
        if borrow_book in self.books:
            print('Get your Book')
            self.books.remove(borrow_book)
        else:
            print('Book not Available')

    def recieve_book(self, receive_book):
        print('You have returned the Book')
        self.books.append(receive_book)

books = ['C', 'C++', 'Java']
o = library(books)

msg = """
    1. Display the Books
    2. Borrow Book
    3. Return Book
"""
while True:
    print(msg)
    choice = int(input('Enter your choice: '))
    if choice==1:
        o.list_books()
    elif choice==2:
        book = input('Enter the Book to Borrow: ')
        o.borrow_book(book)
    elif choice==3:
        book = input('Enter the Book to Return: ')
        o.recieve_book(book)
    else:
        print('Thankyou come again')
        quit()