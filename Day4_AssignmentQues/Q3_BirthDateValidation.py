import re
from datetime import date

try:
    dob = input("Enter DOB (YYYY-MM-DD): ")

    if re.match(r"\d{4}-\d{2}-\d{2}", dob):
        year, month, day = map(int, dob.split("-"))
        today = date.today()
        age = today.year - year
        print("Age:", age)
    else:
        print("Invalid Format")

except:
    print("Error in date input.")