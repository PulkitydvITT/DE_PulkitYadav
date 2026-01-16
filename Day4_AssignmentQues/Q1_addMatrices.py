try:
    r = int(input("Enter rows: "))
    c = int(input("Enter columns: "))

    a = []
    b = []

    print("Enter first matrix:")
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input()))
        a.append(row)

    print("Enter second matrix:")
    for i in range(r):
        row = []
        for j in range(c):
            row.append(int(input()))
        b.append(row)

    print("Sum of matrices:")
    for i in range(r):
        for j in range(c):
            print(a[i][j] + b[i][j], end=" ")
        print()

except:
    print("Invalid input")
