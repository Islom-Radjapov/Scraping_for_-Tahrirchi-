from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import random
from list_useragent import UserAgent

# settings brawser
def setting():
    options = webdriver.ChromeOptions()
    options.add_argument('--window-size=1920,1080')
    options.add_argument(random.choice(UserAgent))
    return webdriver.Chrome(ChromeDriverManager().install(), options=options)

# get new news title
def get_new_title():
    driver = setting()
    driver.get('https://kun.uz/uz')
    WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.CLASS_NAME, 'news-lenta__title')))
    title = driver.find_element(By.CLASS_NAME, 'news-lenta__title').text
    driver.close()
    return title
