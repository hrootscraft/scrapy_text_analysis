<h3>INSTRUCTIONS</h3>

This project scrapes articles from given list of URLs (assignment/Input.csv) and then performs text analysis on the articles obtained to output those metrics in an xlsx file (assignment/output.xlsx)
<br>
In a gist, you run the following commands to get the end result:
Assuming you are in the root directory,

```
cd article_scraper/
scrapy crawl article_spider -L WARN -o ../assignment/output.json
cd ../assignment/
python3 main.py
python3 get_xl_output.py
```

To save the article text into separate files with URL_ID as their names and all these files into one folder in one folder named *article_texts*, run the following command from assignment/ :

```
python3 save_articles.py
```
