# Scraping_for_-Tahrirchi-
Especially scraping for the "Tahrirchi"

I chose kun.uz for information because it is in Uzbek. my program always works because when there is news, it immediately saves the news as a data structure to the sqlite repository.

I didn't separate the words, that would be a mistake, because there is no point in repeating the same information,

if you type "python get_data_to_csv.py" in terminal to get data, it will give you data in "Data.cvs" format,
Note that if you use this code, our sqlite repository will be flushed, that is, after the data is moved to cv, the old one will be deleted.

Yes, it's not a good way to collect data, but I've done it in my time, I think the best way to collect data is a NoSql database.

I extracted the words from the data collected in Jupyter notebook and analyzed them.
I knew I needed to clean words, but now I know better, I need a good function to clean words
