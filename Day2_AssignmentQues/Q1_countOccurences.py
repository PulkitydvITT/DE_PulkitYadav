string = "Hello, ITT!"

char_count = {}

for char in string:
    if char in char_count:
        char_count[char] += 1
    else:
        char_count[char] = 1

print(char_count)
print(string.replace("H", "Y"))
print(string)
