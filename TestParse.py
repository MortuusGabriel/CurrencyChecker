import requests
from bs4 import BeautifulSoup

URL = 'https://bcs-express.ru/kotirovki-i-grafiki/aapl'
HEADERS = {'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/85.0.4183.121 Safari/537.36', 'accept': '*/*'}


def get_html(url, params=None):
    full_page = requests.get(url, headers=HEADERS, params=params)
    return full_page

def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')


    currency = []
    currency.append({
        'name': soup.find_all('h1', class_='quote-head__name')[0].get_text(),
        'price': soup.find_all('div', class_='quote-head__price-value js-quote-head-price js-price-close')[0].get_text(),
        'procents': soup.find_all('div', class_='quote-head__price-change js-profit-percent')[0].get_text(),
        'daily change': soup.find_all('div', class_='quote-head__table-cell')[13].get_text(strip = True).replace('\n                                            ', ''),
    })
    print(currency)

    return(currency)

def parse():
    html = get_html(URL)
    if html.status_code == 200:
        get_content(html.text)
    else:
        print('Request error!')

parse()





# soup = BeautifulSoup(full_page.content, 'html.parser')
#
# convert = soup.findAll("/span", {"class": "highlight-2G-RjaYb price-2c9Z6Fl0"})
# print(convert)