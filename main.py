import json
import os #to check if the file exists
#Import the classes from different files

class Book: 
    def __init__(self, title, author, pages, genre):
        self.title = title
        self.author = author
        self.pages = pages
        self.read = False
        self.price = 0
        self.count = 0
        self.genre = genre

    def setTitle(self, title): #Set the title of the book
        self.title = title
    
    def setAuthor(self, author): #set the author of the book
        self.author = author
    
    def setPages(self, pages): #Set the amount of pages in the book
        self.pages = pages

    def setPrice(self, price): #set the price of the book
        self.price = price
    
    def getTitle(self): #Get the title of the book
        return self.title
    
    def getAuthor(self): #Get the author of the book
        return self.author
    
    def getPages(self): #Get the amount of pages in the book
        return self.pages
    
    def getPrice(self): #Get the price of the book
        return self.price
    
    def markAsRead(self, read): #Set the read to True if read
        self.read = True

    def setGenre(self, genre): #Set the genre of the book
        self.genre = genre
    
    def getGenre(self): #Get the genre of the book
        return self.genre
    
    def purchased(self, count): #collects the amount of time a book has been purchased
        self.count += count

    def getCount(self): #get the amount of times the book has been purchased
        return self.count

    def description(self): #Print out the description
        return (f"Title:{self.title} \nAuthor:{self.author} \nPages:{self.pages} \nGenre:{self.genre if self.genre else 'Not Specific'} \nRead:{self.read} \nPrice:{self.price} \nPurchases:{self.count}")

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

purchasedBooks = {}

def books(): #This function is to housed all of the books in the store
    
    #Setting the books
    mansfieldPark = Book("Mansfield Park", "Jane Austen", "488", "Romance")
    grimmsFairyTales = Book("The Complete Grimm's Fairy Tales", "Jacob Grimm", "880", "Folklore")
    arabianNights = Book("The Arabian Nights", "Unknown", "1049", "Folklore")
    islandOfDrMoreau = Book("The Island of Dr. Moreau", "H.G. Wells","160", "Horror")
    draculasQuest = Book("Dracula's Guest", "Bram Stoker", "20", "Horror")
    authurAndHisKnights = Book("King Arthur and His Knights: Selected Tales", "Thomas Malory", "272", "Historical Fiction")
    maryPoppinsComesback = Book("Mary Poppins Comes Back", "P.L. Travers", "312", "Children's Literature")    
    oedipusCycle = Book("The Oedipus Cycle: Oedipus Rex, Oedipus at Colonus, Antigone", "Sophocles", "259", "Tragedy")
    oPioneers = Book("O Pioneers!", "Willa Cather", "159", "Historical Fiction")    
    
    #Setting Prices for the books
    mansfieldPark.setPrice(29.99)
    grimmsFairyTales.setPrice(59.99)
    arabianNights.setPrice(59.99)
    islandOfDrMoreau.setPrice(24.99)
    draculasQuest.setPrice(24.99)
    authurAndHisKnights.setPrice(29.99)
    maryPoppinsComesback.setPrice(29.99)
    oedipusCycle.setPrice(19.99)
    oPioneers.setPrice(19.99)
    
    #Adding the books to a booklist and return the booklists
    booklists = [mansfieldPark, grimmsFairyTales, arabianNights, islandOfDrMoreau, draculasQuest, authurAndHisKnights, maryPoppinsComesback, oedipusCycle, oPioneers]
    return booklists


def userInput(prompt="Enter a number: "):#This will get the user to enter in a number to make everything run without extra lines
    try: #It will try to return the input with prompt
        return int(input(prompt))
    except ValueError: #Or it will enter in a value error and return -1
        print("Invalid input. Please enter a number.")
        return -1

def carting(booklists): #This is the shopping cart for the bookstore
    global purchasedBooks
    cart = [] #The cart lists
    while True: 
        #this will get the user input from the bookstore. User must select the corresponding numbers to the item (EX: 1. mansfieldpark)
        user = userInput("Select the number of the book to add to your cart (0 to stop): ")
        #if user select 0 it will break the while loop
        if user == 0:
            break
        #if the user is greater than 1 and less than the total amount of books in the booklists.
        #it will select the book item in the list and add it to the cart
        elif 1 <= user <= len(booklists):
            selected = booklists[user - 1]
            cart.append(selected)
            if selected.getTitle() in purchasedBooks:
                purchasedBooks[selected.getTitle()] += 1
            else:
                purchasedBooks[selected.getTitle()] = 1

    return cart 

def displayTop3(): #This will display the top 3 purchased books in the bookstore. 
    print("Top 3 Purchased Books")
    if purchasedBooks:
        sortedBooks = sorted(purchasedBooks.items(), keys = lambda x: x[1], reverse= True)
        for i, (books, count) in enumerate(sortedBooks[:3], 1):
            print(f"{i},{books} - purchased {count} times")
    else:
        print("No books have been purchaseds at this moment.")

def bookstore(): #This is the bookstore... a place to buy books
    total = 0 #Setting the total to 0
    print("What books would you like to buy?")
    print("Press 0 to end shopping list")
    
    #Getting the books for the book list
    booklists = books()
    
    #for the index and book when the booklist is enumerated it will print each book.
    for index, book in enumerate(booklists, 1):
        print(f"{index}. {book.description()}")

    #The cart will be sent back and add up all the prices of the books then print them out and returning the cart again
    cart = carting(booklists)
    total = sum(book.getPrice() for book in cart)

    print(f"Total Amount: ${total:.2f} \nTotal Items: {len(cart)}")
    return cart

def savePurchasedBooks(purchasedBooks): #This will send the books in the purchased books dictionary to a json file to be saved once the user has exited the program
    data = [{"Title": title, "Count": count} for title, count in purchasedBooks.items()]
    with open("purchasebooks.json", "w" ) as file:
        json.dump(data, file, indent=4) #Using Json file to store the list

def loadPurchasedBooks(): #This function will load the purchased books from the json file
    if not os.path.exists("purchasebooks.json"): #this is here to make sure that the file exists
        return {}
    with open("purchasebooks.json", "r" ) as file:
        data = file.load(file) #Using Json file to load the list back into the list
    return {item["Title"]: item["Count"] for item in data}


def searchbyAuthor(booklist, author): #This function will be searched by the Author
    results = [book for book in booklist if book.getAuthor().lower() == author.lower()]
    
    if results: 
        print(f"Books by {author}:")
        for books in results:
            print(books.description())
    else:
        print(f"Books are not found by {author}")
    
def searchbyTitle(booklist, title): #This function will be searched by the title
    sortedBooks = sorted(booklist, key=lambda book: book.getTitle().lower())
    
    leftIndex = 0
    rightIndex = len(sortedBooks) - 1
    
    while leftIndex <= rightIndex:
        mid = (leftIndex + rightIndex) // 2
        midTitle = sortedBooks[mid].getTitle().lower()
        
        if midTitle == title.lower():
            print(f"Book Found: \n{sortedBooks[mid].description()}")
            return sortedBooks[mid]
        elif midTitle < title.lower():left = mid + 1
        else: right = mid + 1
        
    print(f"No Books found with {title}")
    
    return None

def searchbyGenre(booklist, genre): #This function will search through the filtered genre booklist
    results = [book for book in booklist if book.getGenre().lower() == genre.lower()]
    
    if results:
        print(f"Books by {genre}:")
        for books in results:
            print(books.description())
    else:
        print(f"Books are not found by {genre}")
        
def filterByGenre(booklist, genre): #This will function will filtered through by genre and return it
    genres = {book.getGenre() for book in booklist}
    print(f"Avaliable Genres")
    for genre in sorted(genres):
        print(f"- {genre}")
    return sorted(genres)
    
def search(booklist): #This is a search multifunction or a junction to give more room for people to search specifly to their needs
    while True:
        
        print(f"What would you like to search by? \n1. Author \n2. Title \n3. Genre \n4. Go back to Main Menu") #This is a menu to help users choose what they want to search for or they cant press 4 to go back
        user = userInput() #if user inputs a integer variable 
        if user == 1: #if user press 1 it will do a linear search for the authors within the books avaliable
            author = input("Enter in the Author's name here") #by using the user's choice of input
            searchbyAuthor(booklist, author) #it will given to the searchbyAuthor function to help search throughout the list
        elif user == 2: #if user press 2 it will do a binary search to help the user locate books depending on their choice of title
            title = input("Enter in the Title here")
            searchbyTitle(booklist, title)
        elif user == 3: #If user press 3, the program will search through the avaliable genres first then gave the choice to the user to search for what genres they wanted 
            avaliable = filterByGenre(booklist)
            genre = input("Enter in the Title here")
            if genre.lower() in [g.lower() for g in genre]: #if that genre is in the list then it will search through that list then print out that book for the genre
                searchbyGenre(booklist, genre)
            else: #else it will would give this error
                print("Invalid genre")
            
        elif user == 4: #pressing 4 will make the user go back to the previous menu
            break
        else: #Would give a valueerror if you press a wrong input
            print(ValueError)

def choices(person): #This is more so what do the person or user want to do as Choices. This is like what do you want to do such as Read a book, Buy a book, or check your collection of books.
    global purchasedBooks
    while True:
        print(f"What do you want to do? \n1. Read a book in your list? \n2. Buy a book from a bookstore \n3. View your book collection \n4. Get the Top Sold Books \n5. Search and Filtered through the collection \n6. Exit")
         
        #This will get the menu to work
        user = userInput()
        
        #if the user selected 1 and if there are books in the list 
        if user == 1:
            if person.getBooklist():
                #It will print the collection and you can select what you want to read and it will mark it as read by the end
                print("Book Lists in Collection")
                for index, book in enumerate(person.getBooklist(), 1):
                    print(f"{index}. {book.description()}")
                    book_to_read = userInput("Enter the number of the book to read: ") - 1
                    person.readBook(book_to_read)
            else:
                #Else there is no books in the list
                print("You don't have any books to read.")
        
        #If user select 2
        elif user == 2:
            #The User will go to the "Bookstore" and for each item in the list it will add them to the person's book collection and print the total books in the list
            cart = bookstore()
            for item in cart: 
                person.addBook(item)
            print(f"\nYou have purchased {len(cart)} books.")

        #If user select 3
        elif user == 3:
            #it will print out the person's collection
            print(person)

        #If user select 4
        elif user == 4: 
            #it will display top 3 to most Purchased Items:
            displayTop3()

        #If user select 5
        elif user == 5:
           #It will searched 
            print("Search")
            search(person.getBooklist())

        #If user select 6
        elif user == 6:
            #It will end the loop which should end the program
            savePurchasedBooks(purchasedBooks)
            break
        else:
            #Else it will be an invalid option
            print("Invalid option. Please try again.")

def main():
    #Getting the person's name to make it more personal to the user
    global purchasedBooks  #Giving this a global variable will spread the books in stocked throughout the program
    loadData = loadPurchasedBooks() #This will load the data once everything is loaded
    personName = input("Enter in your name here!") #The user will give their name here
    person = Person(personName) #the person's name will be created as a person
    try:
        #Give the person some choices to make
        choices(person) #the person will enter in a choice menu
        print("program ended") #the program prompt telling the user that the program has ended
    except ValueError: #Print out an ValueError if encountered
        print("ValueError")
    except IOError: #Print out an IOError if encountered
        print("ValueError")
    except FileNotFoundError: #Print out an FileNotFoundError if the Person and Book Class file is NOT found...
        print("ValueError")

main()

