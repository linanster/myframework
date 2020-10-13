import requests

url = "http://localhost:4000/api/test/test13"

payload = {}
files = {}
headers= {}

response = requests.request("GET", url, headers=headers, data = payload, files = files)

print('==type of response.content==', type(response.content))

with open('./1.data', 'wb') as myfile:
    myfile.write(response.content)

