import requests
import pprint

response = requests.get('https://www.oboilux.ru/wallpapers/zuber/park-avenue')

params = {
    'q': 'html'
}

response = requests.get( 'https://api.github.com/search/repositories', params=params)

print(response.status_code)

response_json = response.json()
pprint.pprint(response_json)

print(f"количество репозиториев с использованием html: {response_json['total_count']}")
