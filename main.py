import requests
from bs4 import BeautifulSoup
import json
headers = {
'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.15; rv:123.0) Gecko/20100101 Firefox/123.0',
 'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8',
 'Accept-Language': 'en-US,en;q=0.5',
 'Referer': 'https://mlh.io/',
 'DNT': '1',
 'Connection': 'keep-alive',
 'Upgrade-Insecure-Requests': '1',
}

response = requests.get('https://mlh.io/seasons/2024/events', headers=headers)

soup = BeautifulSoup(response.text, 'html.parser')

events = soup.find_all('div', class_='event-wrapper')
events_mapping = []

for event in events:
    name = event.find('h3', class_='event-name').text
    start_date = event.find('meta', itemprop='startDate')['content']
    end_date = event.find('meta', itemprop='endDate')['content']
    location = event.find('div', class_='event-location').text.strip()
    location = location.replace('\n', '')
    link = event.find('a')['href']

    events_mapping.append({
        'name': name,
        'link': link,
        'start_date': start_date,
        'end_date': end_date,
        'location': location
    })


for event in events_mapping:
    print("Event Name: ", event['name'])
    print("Start Date: ", event['start_date'])
    print("End Date: ", event['end_date'])
    print("Link: ", event['link'])
    print("Location: ", event['location'])
    print("=====================================")
    

    
