import requests
from bs4 import BeautifulSoup
import pandas as pd
from datetime import datetime
from sql_codes import add_data


# function get data all
def request(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'html.parser')

# function get DataFrame
def get_data(new):
    soup = request(new)
    new_date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    title = soup.find('div', class_='single-header__title').get_text()
    contents = soup.find('div', class_='single-content')
    try:
        content = contents.find('h4').get_text()
    except:
        content = ""
    contents_p = contents.find_all('p')
    for x in contents_p:
        content += " " + x.get_text()
    return pd.DataFrame({'url': new,
                         'date': new_date,
                         'title': title,
                         'content': content}, index=[0])

# takes the latest article from kun.uz and saves it database
def Scraping_new_data(kun_uz):
    soup = request(kun_uz)
    urls = soup.find_all('div', class_='mb-25')
    new_url = 'https://kun.uz' + urls[0].find_all('a')[0].get('href')
    df = get_data(new_url)
    add_data(df.url.values[0], df.date.values[0], df.title.values[0], df.content.values[0])
