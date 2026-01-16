length = int(input("Enter the minimum length required for password : "))
password = input("Enter the password : ")

specialCharacters = "!\"#$%&'()*+,-./:;<=>?@[\\]^_`{|}~"
digit = 0
specialCharacter = 0

for char in password:
    if char.isdigit():
        digit = 1
    if char in specialCharacters:
        specialCharacter = 1

if(len(password) >= length and digit and specialCharacter):
    print("Valid Password")
else:
    print("Not a valid password")