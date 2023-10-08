import requests

import time

from bs4 import BeautifulSoup

YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'


# Doesnt execute javaScript
response = requests.get(YOUTUBE_TRENDING_URL)

print('Status Code', response.status_code)


# with open('trending.html', 'w') as f:
#   f.write(response.text)
time.sleep(3)

doc = BeautifulSoup(response.text, 'html.parser')

print('Page title:', doc.title.text)

video_divs = doc.find_all('div', class_='ytd-video-renderer')

print(f'Found {len(video_divs)} videos')