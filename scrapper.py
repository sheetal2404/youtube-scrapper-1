from selenium import webdriver


YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'


driver = webdriver.Chrome()

driver.get(YOUTUBE_TRENDING_URL)

print('Page Title: ', driver.title)