import requests
from bs4 import BeautifulSoup

def load_html(url):
    response = requests.get(url)
    return response.text

def get_title_rows(html):
    soup = BeautifulSoup(html, 'html.parser')
    return soup.find_all('tr', class_='athing')

def get_titles(rows):
    return [row.find('span', class_='titleline').find('a').text for row in rows]

def get_links(soup):
    links = []
    for link in soup.find_all('a'):
        links.append(link.get('href'))
    return links

html = load_html('https://news.ycombinator.com/')
rows = get_title_rows(html)
titles = get_titles(rows)
print(titles)

links = get_links(BeautifulSoup(html, 'html.parser'))
print(links)
