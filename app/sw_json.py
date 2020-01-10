import requests
from bs4 import BeautifulSoup
import time
import csv


def get_html(url):
    r = requests.get(url)
    if r.ok:
        return r.text
    print(r.status_code)


def write_csv(data):
    with open('/home/black/Desktop/synthway/app/sw.csv', 'w', encoding='utf8') as f:
        writer = csv.writer(f)
        writer.writerows(data)


def get_playlist(html):
    soup = BeautifulSoup(html, 'lxml')

    table = soup.find_all('table')[1]
    trs = table.find_all('tr')

    playlist = []

    for tr in trs[1:]:
        tmp_lst = []
        name = tr.find_all('td')[1].text.strip()
        tmp_lst.append({'track_name': name})
        playlist.append(tmp_lst)

    write_csv(playlist)


def main():
    url = 'http://s5.radioboss.fm:8380/played.html?sid=1'
    r = requests.get(url)

    while True:
        if r.ok:
            get_playlist(get_html(url))
            time.sleep(10)
        else:
            break


if __name__ == '__main__':
    main()
