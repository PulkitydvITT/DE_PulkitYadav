data = {
    "America": 10,
    "Britain": 5,
    "Australia": 7,
    "Canada": 3
}

filtered_dict = {k: v for k, v in data.items() if k.startswith('A')}
print(filtered_dict)