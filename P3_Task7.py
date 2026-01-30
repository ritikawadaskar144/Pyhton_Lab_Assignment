start = int(input("Enter starting number: "))
end = int(input("Enter ending number: "))

while start > end:
    print("Starting number must be smaller than ending number.")
    start = int(input("Enter starting number again: "))
    end = int(input("Enter ending number again: "))

print("Prime numbers are:")

for num in range(start, end + 1):
    if num > 1:
        is_prime = True
        for i in range(2, num):
            if num % i == 0:
                is_prime = False
                break
        if is_prime:
            print(num, end=" ")
