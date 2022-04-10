import requests

endpoint = "http://127.0.0.1:8000/api/products/"

data = {
    "title":"This is title"
}
get_response = requests.get(endpoint,json = data)

print(get_response.json())
