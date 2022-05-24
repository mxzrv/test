

from bs4 import BeautifulSoup
import requests

url = 'https://dtf.ru/gamedev'
def get_news(url):
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('div', class_='content-title content-title--short l-island-a')
    for el in news:
        print(el.text.replace('\n' + ' ' * 36, ''))

get_news(url)
