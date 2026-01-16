try:
    numbers = [1, 2, 3, 4, 5]
    result = list(map(lambda x: (x + 10) ** 2, numbers))
    print(result)
except Exception as e:
    print("Unexpected error:", e)