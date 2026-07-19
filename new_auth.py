import httpx

login_payload = {
  "email": "test@test.ru",
  "password": "Test1234!"
}

login_response = httpx.post("http://localhost:8000/api/v1/authentication/login", json=login_payload)
login_response_data = login_response.json()

print("Login response: ", login_response_data)
print("Status_code: ", login_response.status_code)

headers_access_token = {"Authorization": "Bearer " + login_response_data['token']['accessToken']}

get_user = httpx.get("http://localhost:8000/api/v1/users/me", headers=headers_access_token)
get_user_data = get_user.json()

print("Данные пользователя: ", get_user_data)
print("Status_code: ", get_user.status_code)
