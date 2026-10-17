from books import show_books, load_books, save_books

name = input("Enter your name: ")
print("Welcome to Personal Book Manager,", name)

books = load_books()

print("Your saved books:")
show_books(books)

number = int(input("How many new books do you want to add? "))

for i in range(number):
    book = input("Enter the name of book: ")
    books.append(book)

save_books(books)

print("All your books:")
show_books(books)
