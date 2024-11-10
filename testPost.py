import requests

url = "http://127.0.0.1:8000/login"
data = {
    "username": "user1",
    "password": "password1"
}

response = requests.post(url, json=data)

# Verifica la respuesta
if response.status_code == 200:
    print(response.json())  # Imprime {"message": "Login successful", "session_token": "token_user1"}
else:
    print("Error:", response.status_code, response.json())
