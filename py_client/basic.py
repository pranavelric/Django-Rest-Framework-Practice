import requests

# endpoint = "https://httpbin.org/anything"
endpoint = "http://127.0.0.1:8000/api/v2/products/"

get_response = requests.get(endpoint)
# get_response2 = requests.post(endpoint, params={"abc":123},json={"title":"hello","query":"Hello world"})

print(get_response.json())
