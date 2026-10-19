import requests
## Reshape and Save
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(response.status_code)
if response.status_code == 200:
    data = response.json()
    clean_users = []
    clean_user = {
        "userId": data["userId"],
        "id": data["id"],
        "title": data["title"]       
    }
    clean_users.append(clean_user)
    print(data)
    print(clean_users)
else:
 print("Request failed")
 print(response.text)