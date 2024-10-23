from Book import *
#import the book class over to make this Person class functional

class Person:
    def __init__(self, name):
        self.name = name
        self.booklist = []
    
    def addBook(self, book): #Will append the book to the booklist
        self.booklist.append(book)

    def getBooklist(self): #will print out the booklsit 
        return self.booklist

    def readBook(self, index):#Check if the book is read
        if index < len(self.booklist):
            book = self.booklist[index]
            book.markAsRead(True)
        
    def __str__(self): #Print out the statements and books
        if not self.booklist:
            return f"{self.name} has no books in their collection"
        books_str = ', '.join([book.getTitle() for book in self.booklist])
        return f"{self.name}'s book collection: {books_str}"