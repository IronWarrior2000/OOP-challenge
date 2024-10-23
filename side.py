from Book import *
#imported the book class to make this file functional

def main():
    #Set books
    theSun = Book("The Sun", "John Doe", "300", "Supernatural")
    theMoon = Book("The Moon", "John Doe", "210", "Supernatural") 
    theSun.markAsRead(True)

    booklist = [theSun, theMoon]
    
    for items in booklist:
        print(items.description())
    return booklist

main()