import httpx

# response = httpx.get('https://jsonplaceholder.typicode.com/todos/1')
#
# print(response.status_code)
# print(response.json())
#
# data = {
#     "title": "Новая задача",
#     "completed": False,
#     "userId": 1
# }
#
# response = httpx.post('https://jsonplaceholder.typicode.com/posts', json=data)
#
# print(response.status_code)
# print(response.json())


# data = {"username": "Test_user", "password": "12345"}
#
# response = httpx.post("http://httpbin.org/post", data=data)
#
# print(response.status_code)
# print(response.json())


# headers = {"Authorization": "Bearer my_secret_token"}
# response = httpx.get("http://httpbin.org/get", headers=headers)
#
# print(response.request.headers)
# print(response.json())
#
# params = {"userId": 1, "id": 1}
# response = httpx.get("https://jsonplaceholder.typicode.com/todos", params=params)
#
#
# print(response.url)
# print(response.json())
# print()
#
# files = {"file": ("example.txt", open("example.txt", "rb"))}
# response = httpx.post("http://httpbin.org/post", files=files)
#
# print(response.json())

# with httpx.Client() as client:
#     response1 = client.get("https://jsonplaceholder.typicode.com/todos/1")
#     response2 = client.get("https://jsonplaceholder.typicode.com/todos/2")
#
#
# print(response1.json())
# print(response2.json())

# client = httpx.Client(headers={"Authorization": "Bearer my_secret_token"})
# response = client.get("http://httpbin.org/get")
#
# print(response.json())

# response = httpx.get("https://jsonplaceholder.typicode.com/invalid_url")
# print(response.status_code)


try:
    response = httpx.get("https://jsonplaceholder.typicode.com/invalid_url")
    response.raise_for_status()
except httpx.HTTPError as e:
    print(f"Ошибка запроса: {e}")


try:
    response = httpx.get("http://httpbin.org/delay/5", timeout=2)
except httpx.ReadTimeout:
    print("Запрос превысил лимит времени")





