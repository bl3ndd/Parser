from bs4 import BeautifulSoup
import requests
import json


with open('data/quotes_and_author.json', 'r', encoding='utf-8') as file:
    json_list = json.loads(file.read())
authors = []
for i in range(len(json_list) - 1):
    author_name = json_list[i - 1]['Author']
    if author_name not in authors:
        authors.append(json_list[i - 1]['Author'].replace(' ', '-').replace('.-', '-').replace('.', '-').replace('é', 'e').replace('Dr Seuss', 'Dr-Seuss').replace('Martin-Luther-King-Jr-', 'Martin-Luther-King-Jr'))

all_author_info = []
authors = set(authors)
authors = list(authors)
print(authors)

for author in authors:
    url = f'http://quotes.toscrape.com/author/{author}/'

    site_request = requests.get(url)
    src = site_request.text
    soup = BeautifulSoup(src, 'lxml')
    all_info = soup.find(class_='author-details')
    name = all_info.find(class_='author-title')
    birth = all_info.find(class_='author-born-date')
    place = all_info.find(class_='author-born-location')
    biography = all_info.find(class_='author-description')

    all_author_info.append(
        {
            'Name': name.text.strip(),
            'Birth': birth.text,
            'Place': place.text,
            'Biography': biography.text.strip()
        }
    )

    with open(f'data/about_author.json', 'w', encoding='utf-8') as file:
        json.dump(all_author_info, file, indent=4, ensure_ascii=False)