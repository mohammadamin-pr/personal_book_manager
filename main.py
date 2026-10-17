from books import show_books

name = input("Enter your name: ")
print("Welcome to Personal Book Manager,", name)

number = int(input("How many books do you want to add? "))

books = []

for i in range(number):
    book = input("Enter the name of book: ")
    books.append(book)

show_books(books)
