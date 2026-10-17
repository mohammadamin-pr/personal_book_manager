name = input("Enter your name: ")
print("Welcome to Personal Book Manager,", name)

number = int(input("How many books do you want to add? "))

books = []

for i in range(number):
    book = input("Enter the name of book: ")
    books.append(book)

print("Your books: ")

for book in books:
    print(book)
