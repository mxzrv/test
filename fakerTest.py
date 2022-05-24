from bs4 import BeautifulSoup
import requests

url = 'https://habr.com/ru/all/'
def get_news(url):
    response = requests.get(url)

    soup = BeautifulSoup(response.text, 'html.parser')
    news = soup.find_all('a', class_='tm-article-snippet__title-link')
    for el in news:
        print(el.find('span').text)

for i in range(1, 11):
    get_news('https://habr.com/ru/all/page' + str(i))


