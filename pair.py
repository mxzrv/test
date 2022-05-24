import requests



def get_weather_by_city(city_name):
    url = 'https://goweather.herokuapp.com/weather/' + city_name
    weather = requests.get(url).json()
    return weather

def print_fun_facts():
    url = 'https://cat-fact.herokuapp.com/facts'
    for i in range(4):
        print(requests.get(url).json()[i]['text'])

print_fun_facts()

url = 'https://openlibrary.org/authors/OL33421A.json'
print(requests.get(url).json())
