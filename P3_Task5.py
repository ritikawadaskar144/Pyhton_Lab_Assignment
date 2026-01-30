rows = 5

for i in range(rows):
    for space in range(i):
        print(" ", end="")
    for star in range(rows - i):
        print("* ", end="")
    print()
