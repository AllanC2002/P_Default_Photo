import requests

BASE_URL = "http://107.21.24.33:8080"
user_id = 12

# Enviar user_id en JSON (body) porque el endpoint lo espera así
response = requests.post(f"{BASE_URL}/default-photo", json={"Id_User": user_id})

print(response.status_code)
print(response.text)
