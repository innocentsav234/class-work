from datetime import datetime
from pathlib import Path
import os
import json
num = [1, 2, 10]
total = sum(num)
print(total)

time = datetime.now()
print(time)

file = Path("oop.py")
print(file.exists())

user_name = os.getenv("USERNAME")
print(user_name)

try:
    age = int(input("Enter your age: "))
except ValueError:
     print("this is an invalid age") 

text = "our God is great"
with open("student.json", 'w') as file:
     json.dump(text, file)

with open("student.json", 'r') as file:
     load = json.load(file)
     print(load)     

