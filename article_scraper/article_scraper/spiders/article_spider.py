import pandas as pd
import scrapy
import json
import os


class ArticleSpider(scrapy.Spider):
    name = 'article_spider'
    allowed_domains = ['insights.blackcoffer.com']

    def start_requests(self):
        # Get the path of the current file (article_spider.py)
        current_path = os.path.abspath(__file__)
    
        # Get the directory path of the current file
        directory_path = os.path.dirname(current_path)
    
        # Construct the relative path to Input.csv
        csv_path = os.path.join(directory_path, '..', '..', '..', 'assignment', 'Input.csv')
    
        # Read the CSV file and extract the URLs
        df = pd.read_csv(csv_path)
        df_json_list = df.to_dict(orient='records')

        # Start scraping each URL
        for item in df_json_list:
            yield scrapy.Request(url=item['URL'], meta={'item': item}, callback=self.parse)

    def parse(self, response):
        item = response.meta['item']

        content_type = response.headers.get(
            'Content-Type', b'').decode('utf-8').lower()

        # Handle JSON response
        if 'application/json' in content_type:
            try:
                data = json.loads(response.body)
                item['title'] = data.get('title')
                item['body'] = data.get('body')
                print(data)
            except json.JSONDecodeError:
                self.logger.error('Failed to decode JSON response')
        elif 'text/html' in content_type:
            # Handle HTML response
            title = response.css('h1::text').get()
            body = response.css('.td-post-content p::text').getall()
            body = ' '.join(body)
            
            item['title'] = title
            item['body'] = body

            yield item
        else:
            self.logger.error('Unknown Content-Type: %s', content_type)