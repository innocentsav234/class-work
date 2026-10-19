import json
from urllib.request import urlopen

url = "https://jsonplaceholder.typicode.com/users"

# Fetch the API data and convert the JSON response into Python data
with urlopen(url) as response:
    users = json.load(response)

# Keep only the fields required for the assignment
reshaped_users = [
    {
        "name": user["name"],
        "email": user["email"],
        "city": user["address"]["city"],
    }
    for user in users
]

# Save the reshaped data to users.json
with open("users.json", "w", encoding="utf-8") as file:
    json.dump(reshaped_users, file, indent=2)

# Open the saved file and print its contents
with open("users.json", "r", encoding="utf-8") as file:
    print(file.read())