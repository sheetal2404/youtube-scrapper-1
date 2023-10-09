from selenium import webdriver
import pandas as pd


YOUTUBE_TRENDING_URL = 'https://www.youtube.com/feed/trending'

# Specify the path to the ChromeDriver executable
chrome_driver_path = 'C:\\Users\\hp\\Desktop\\chromedriver-win64(2)\\chromedriver-win64\\chromedriver.exe'

details_videos = []


def get_driver():
    # Initialize the Chrome WebDriver with options
    chrome_options = webdriver.ChromeOptions()
    chrome_options.add_argument('--disable-dev-shm-usage')
    chrome_options.add_argument('--headless')  # Add headless mode if needed

    # Use the specified ChromeDriver executable path
    driver = webdriver.Chrome(executable_path=chrome_driver_path,options=chrome_options)
    return driver


def get_videos(driver):
    VIDEO_DIV_TAG = 'ytd-video-renderer'
    driver.get(YOUTUBE_TRENDING_URL)
    video_divs = driver.find_elements_by_tag_name(VIDEO_DIV_TAG)
    return video_divs


def parse_video(n,video):
    detail_video = {}

    title_tag = video.find_element_by_id('video-title')
    title = title_tag.text
    url = title_tag.get_attribute('href')

    thumbnail_tag = video.find_element_by_tag_name('img')
    thumbnail_url = thumbnail_tag.get_attribute('src')

    channel_div = video.find_element_by_class_name('ytd-channel-name')
    channel_name = channel_div.text

    view_time_div = video.find_element_by_id('separator')
    view_time = view_time_div.text

    description = video.find_element_by_id('description-text').text

    detail_video = {'Title':title, 'URL':url, 'Thumbnail URL':thumbnail_url, 'Channel':channel_name, 'Description': description}
    details_videos.append(detail_video)


if __name__ == "__main__":
    print('Creating Driver...')
    driver = get_driver()

    print('Fetching the videos>>>')
    videos = get_videos(driver)

    print(f"Found {len(videos)} videos")
    print('Parsing....')

    for i in range(10):
        video = videos[i]
        parse_video(i+1,video)

    #print(details_videos)

    # print("Title: "+title)
    # print("URL: "+url)
    # print('Thumbnail URL: '+thumbnail_url)
    # print('Channel Name: '+channel_name)
    # print('Description: '+description)
    # print('Views and Time: '+view_time)

    print("Save the data to a CSV file...")
    videos_df = pd.DataFrame(details_videos)
    print(videos_df)
    videos_df.to_csv('trending.csv', index=None)


