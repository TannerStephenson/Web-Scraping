import requests
import pandas as pd
from bs4 import BeautifulSoup

website = 'http://quotes.toscrape.com/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')


def csv_scrape():
    box = soup.find_all('div', class_='quote')

    quotes = []
    authors = []

    for box in box:
        quote = box.find('span', class_='text').get_text()
        author = box.find('small', class_='author').get_text()
        quotes.append(quote)
        authors.append(author)

    df = pd.DataFrame({'Quote': quotes, 'Author': authors})

    df.to_csv('quotes.csv', index=False)


csv_scrape()


