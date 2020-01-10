import requests
from bs4 import BeautifulSoup


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def get_playlist(html):
    soup = BeautifulSoup(html, 'lxml')

    table = soup.find_all('table')[1]
    trs = table.find_all('tr')

    played_json = []

    for tr in trs[1:]:
        name = tr.find_all('td')[1].text.strip('')
        played_json.append({'title': name})

    return played_json


def main():
    url = 'http://s5.radioboss.fm:8380/played.html?sid=1'
    return get_playlist(get_html(url))
