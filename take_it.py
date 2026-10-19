import requests

# response = requests.get("https://jsonplaceholder.typicode.com/posts/1")
# print(response.status_code)
# print(response)
# data = response.json()
# print(response.headers.get("Content-Type"))
# print(response.text)
# print(data["title"])
# print(data["body"])
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

# url = "https://jsonplaceholder.typicode.com/posts/1"
# response = requests.get(url)
# print(response.status_code)
# if response.status_code == 200:
#     data = response.json()
#     print(data)
# else:
#     print("Request failed")
#     print(response.text)


## Reshape and Save
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.get(url)
print(response.status_code)
if r


#url = "https://jsonplaceholder.typicode.com/posts/1"
#response = requests.get(url)
#print(response.status_code)
#if response.status_code == 200:
#     data = response.json()
#     clean_users = []
#     clean_users.append(data)
#     for user in clean_users:
#         clean_users.remove(data["body"])
#     print(clean_users)
#     print(data)
#else:
#     print("Request failed")
#     print(response.text)



