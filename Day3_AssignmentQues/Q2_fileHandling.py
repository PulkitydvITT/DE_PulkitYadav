def factorial(n):
    try:
        if n < 0:
            raise ValueError("Factorial can't be calculate for negative numbers.")
        if n == 0 or n == 1:
            return 1
        return n * factorial(n - 1)
    except Exception as e:
        print("Factorial Error:", e)

try:
    num = int(input("Enter a number: "))
    result = factorial(num)
    with open("file.txt", "w") as file:
        file.write(f"The factorial of {num} is {result}")

except FileNotFoundError:
    print("Error: File not found.")

except Exception as e:
    print("Unexpected file error:", e)
