for i in range(0,5):
    for space in range(0,5-i):
        print(" ",end=" ")
    for j in range(0,(2*i+1)):
        print("*",end=" ")
    print()