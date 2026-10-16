import os
import json
from pathlib import Path
# API call/agrument:

num = [10, 10, 20, 10]
total = sum(num)
print(total)

# API USING PATH:

file = Path("text.txt")
print(file.exists())

# API operating system:

user_name = os.getenv("USERNAME")
print(user_name)

#json.dupm
text = " is a great day"
with open("kingdom.json", 'w') as file:
    json.dump(text, file)
# json.load
with open("kingdom.json", 'r') as file:
    load = json.load(file)
    print(load)



