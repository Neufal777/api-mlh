import requests
import re

quotes = []

headers = {
    'accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7',
    'accept-language': 'es-ES,es;q=0.9,en;q=0.8',
    'referer': 'https://quotes.toscrape.com/',
    'upgrade-insecure-requests': '1',
    'user-agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/123.0.0.0 Safari/537.36',
}

for i in range(1, 100):
    print("Scraping page", i)
    
    response = requests.get(f'https://quotes.toscrape.com/page/{i}/', headers=headers)
    pattern = r'<span class="text" itemprop="text">([^<]*)'
    matches = re.findall(pattern, response.text)
    
    if "No quotes found!" in response.text:
        print("No more quotes found!")
        break
    else:
        for match in matches:
            quotes.append(match.strip())

with open('quotes_collection.txt', 'w') as f:
    for quote in quotes:
        f.write(quote.strip() + '\n')    