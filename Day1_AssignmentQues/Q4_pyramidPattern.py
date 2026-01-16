rows = int(input("Enter number of rows : "))

for i in range(1, rows + 1):
    
    for spaces in range(rows - i):
        print(" ", end="")

    for stars in range(i):
        print("* ", end="")
    
    print()
