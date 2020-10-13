import requests

url = "http://localhost:4000/api/test/test12"

payload = {}
files = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print(response.json())
