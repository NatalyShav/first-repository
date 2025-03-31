import requests

from params import response

url = "https://jsonplaceholder.typicode.com/posts"

data = {
   'title': 'foo',
    'body': 'bar',
    'userId': 1
}

resource = requests.post(url, data=data)

print(response.status_code)
print(f"Ответ - {response.json()}")