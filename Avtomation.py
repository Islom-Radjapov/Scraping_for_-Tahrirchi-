from testing_new_data import get_new_title
from sql_codes import get_last_title
from time import sleep
from Scraping_new import Scraping_new_data

kun_uz = 'https://kun.uz/uz' # Uzb language url or (/ru)

# main function
while True:
    try:
        new_title = get_new_title().strip()
        last_title = get_last_title().strip()
        if new_title != last_title:
            Scraping_new_data(kun_uz=kun_uz)
    except:
        pass
    # waits every 5 minutes
    sleep(300)

