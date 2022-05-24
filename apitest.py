import requests
import webbrowser

url = 'https://xkcd.com/info.0.json'
weather = requests.get(url).json()
print(weather['month'])

url = 'https://xkcd.com/info.0.json'
weather = requests.get(url).json()
print(weather['year'])

url = 'https://xkcd.com/info.0.json'
print(requests.get(url).json()['title'])

url = 'https://anapioficeandfire.com/api/characters/583'
print(requests.get(url).json()['name'])

url = 'https://anapioficeandfire.com/api/characters/583'
print(requests.get(url).json()['born'])

url = 'https://anapioficeandfire.com/api/characters/583'
print(requests.get(url).json()['titles'])

url = 'https://www.valvesoftware.com/ru/about/stats'
print(requests.get(url).json()['users_online'])

url = 'https://www.valvesoftware.com/ru/about/stats'
print(requests.get(url).json()['users_ingame'])

url = 'https://rickandmortyapi.com/api/character/148'
weather = requests.get(url).json()
print(weather['name'])

url = 'https://rickandmortyapi.com/api/character/148'
weather = requests.get(url).json()
print(weather['gender'])


url = 'https://random-d.uk/api/random'
pic_url = requests.get(url).json()['url']
for i in range(1,3):
    webbrowser.open(pic_url)


    
