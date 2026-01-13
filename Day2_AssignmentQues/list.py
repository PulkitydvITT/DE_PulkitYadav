list = [1, 2, 3, 4]

list.append(5)

list.remove(2)

element = 3
if element in list:
    print(f"{element} is in the list.")
else:
    print(f"{element} is not in the list.")

print("Modified list:", list)