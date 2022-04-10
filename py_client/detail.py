import requests

endpoint = "http://127.0.0.1:8000/api/products/1"

get_response = requests.get(endpoint,json={"query":"Hello world"})
# get_response2 = requests.post(endpoint, params={"abc":123},json={"title":"hello","query":"Hello world"})

print(get_response.json())
