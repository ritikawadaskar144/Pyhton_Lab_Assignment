#Lab_Assignment-1
def add(a, b):
    return a + b

def sub(a, b):
    return a - b

def mul(a, b):
    return a * b

def div(a, b):
    if b == 0:
        return "Cannot divide by zero"
    return a / b

def mod(a, b):
    return a % b

while True:
    print("\n---- CALCULATOR MENU ----")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")
    print("5. Modulus")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 6:
        print("Exiting...")
        break

    num1 = float(input("Enter first number: "))
    num2 = float(input("Enter second number: "))

    if choice == 1:
        print("Result:", add(num1, num2))
    elif choice == 2:
        print("Result:", sub(num1, num2))
    elif choice == 3:
        print("Result:", mul(num1, num2))
    elif choice == 4:
        print("Result:", div(num1, num2))
    elif choice == 5:
        print("Result:", mod(num1, num2))
    else:
        print("Invalid choice!")

#Lab_Assignment-2


balance = 0

def show_balance():
    print("Current Balance:", balance)

def deposit(amount):
    global balance
    balance += amount
    print("Amount Deposited Successfully!")

def withdraw(amount):
    global balance
    if amount > balance:
        print("Insufficient Balance!")
    else:
        balance -= amount
        print("Withdrawal Successful!")


while True:
    print("\n---- BANK MENU ----")
    print("1. Display Balance")
    print("2. Deposit Amount")
    print("3. Withdraw Amount")
    print("4. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 4:
        print("Thank you!")
        break

    elif choice == 1:
        show_balance()

    elif choice == 2:
        amt = float(input("Enter amount to deposit: "))
        deposit(amt)

    elif choice == 3:
        amt = float(input("Enter amount to withdraw: "))
        withdraw(amt)

    else:
        print("Invalid choice!")