#Prctical 9
#Task 1
class Employee:
    def get_data(self):
        self.name = input("Enter Name: ")
        self.age = int(input("Enter Age: "))
        self.salary = float(input("Enter Salary: "))
        self.address = input("Enter Address: ")

    def display(self):
        print("Name:", self.name)
        print("Age:", self.age)
        print("Salary:", self.salary)
        print("Address:", self.address)


class Manager(Employee):
    pass


managers = []

print("Enter details of 2 managers (example):")

for i in range(2):
    print("\nManager", i+1)
    m = Manager()
    m.get_data()
    managers.append(m)

print("\nManager Details")

for i in managers:
    i.display()
    print("------------------")


#Task2
class Book:
    def __init__(self, title):
        self.title = title
        self.available = True


class Library:
    def __init__(self):
        self.books = []

    def add_book(self, title):
        self.books.append(Book(title))
        print("Book added successfully")

    def display_books(self):
        for book in self.books:
            status = "Available" if book.available else "Issued"
            print(book.title, "-", status)

    def lend_book(self, title):
        for book in self.books:
            if book.title == title and book.available:
                book.available = False
                print("Book issued")
                return
        print("Book not available")

    def return_book(self, title):
        for book in self.books:
            if book.title == title:
                book.available = True
                print("Book returned")
                return


library = Library()

while True:
    print("\n1 Add Book")
    print("2 Show Books")
    print("3 Issue Book")
    print("4 Return Book")
    print("5 Exit")

    choice = int(input("Enter choice: "))

    if choice == 1:
        name = input("Enter book name: ")
        library.add_book(name)

    elif choice == 2:
        library.display_books()

    elif choice == 3:
        name = input("Enter book name to issue: ")
        library.lend_book(name)

    elif choice == 4:
        name = input("Enter book name to return: ")
        library.return_book(name)

    elif choice == 5:
        break