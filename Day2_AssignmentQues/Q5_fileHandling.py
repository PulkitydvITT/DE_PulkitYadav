user_input = input("Enter the text : ")

with open("my_file.txt", "w") as file:
    file.write(user_input)

print("Data written Successfully.")