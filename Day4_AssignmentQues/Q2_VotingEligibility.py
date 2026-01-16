try:
    age = int(input("Enter your age: "))

    if age >= 18:
        print("Eligible")
    else:
        print("Not eligible")
except:
    print("Please enter a valid age.")
