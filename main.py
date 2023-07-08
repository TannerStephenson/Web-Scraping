import requests
import pandas as pd
import re
import tkinter as tk
from bs4 import BeautifulSoup

website = 'http://quotes.toscrape.com/'
result = requests.get(website)
content = result.text

soup = BeautifulSoup(content, 'lxml')


def tag_scrape():
    tag = soup.find_all('span', class_='tag-item')
    print("Please choose a tag to sort by:")

    for tag in tag:
        individual_tag = tag.find('a')
        tag_url = individual_tag['href']
        match = re.search(r'tag/(.+)/', tag_url)
        if match:
            print(match.group(1))


def print_console():
    boxes = soup.find_all('div', class_='quote')

    for box in boxes:
        quote = box.find('span', class_='text').get_text()
        author = box.find('small', class_='author').get_text()
        print(quote)
        print(author)


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


def about():
    print()
    print("Hi, my name is Tanner Stephenson.")
    print()
    print("This is a test for python's web scraping capabilities.")
    print("I'm using http://quotes.toscrape.com/ for this test program")
    print()


def menu():
    print("Welcome to my Web-Scraper")
    print("-------------------------")

    choice = input("""'1': "Print to console
'2': "Create and save a csv file
'3': 'Sort by tag'
'4': 'About'
'5': "Exit
Please select: """)
    print(choice)

    if choice == '1':
        print_console()
        print()
        menu()
    elif choice == '2':
        csv_scrape()
        menu()
    elif choice == '3':
        tag_scrape()
        menu()
    elif choice == '4':
        about()
        menu()
    elif choice == '5':
        exit()
    else:
        print("Unknown Option Selected!")


menu()
