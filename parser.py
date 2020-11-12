from bs4 import BeautifulSoup
import requests
import json

page = 1
# url = f'http://quotes.toscrape.com/page/{page}/'
#
# site_request = requests.get(url)
# src = site_request.text

author_quote = []
tag = []


for page in range(10):
    url = f'http://quotes.toscrape.com/page/{page}/'

    site_request = requests.get(url)
    src = site_request.text

    with open(f'index_{page}.html', 'w', encoding='utf-8') as file:
        file.write(src)

    soup = BeautifulSoup(src, 'lxml')

    all_quotes = soup.find_all(class_='quote')



    for item in all_quotes:
        quote = item.find(class_='text')
        author = item.find(class_='author')
        tags = item.find_all(class_='tag')
        for tag_text in tags:
            tag.append(tag_text.text)
        # for tag_item in tags:
        #     tag.append(tag_item.text)
        #     print(tag)
        author_quote.append(
            {
                'Author': author.text,
                'Quote': quote.text,
                'Tags': tag
            }
        )
        tag = []
        with open(f'data/quotes_and_author.json', 'w', encoding='utf-8') as file:
                json.dump(author_quote, file, indent=4, ensure_ascii=False)

