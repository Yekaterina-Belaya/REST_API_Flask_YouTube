import requests

BASE_URL = "http://127.0.0.1:5000/"


response = requests.delete(BASE_URL + "video/2")
print(response)
response = requests.get(BASE_URL + "video/2")
print(response)

