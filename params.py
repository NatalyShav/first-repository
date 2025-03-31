import  requests
import pprint

url = 'https://jsonplaceholder.typicode.com/posts'

params = {
    'userId': 1
}

response = requests.get(url, params=params)

response_json = response.json()

pprint.pprint(response_json)

print(f"Ответ - {response_json}")
