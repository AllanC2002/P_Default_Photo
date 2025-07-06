import requests

#BASE_URL = "http://107.21.24.33:8080" qa
BASE_URL = "http://44.210.210.33:8080"
user_id = 3

response = requests.post(f"{BASE_URL}/default-photo", json={"Id_User": user_id})

print(response.status_code)
print(response.text)
