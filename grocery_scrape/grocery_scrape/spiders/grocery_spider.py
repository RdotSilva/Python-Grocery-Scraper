import scrapy


class GrocerySpider(scrapy.Spider):
    """Class to crawl Grocery pages"""

    name = "grocery"

    start_urls = ["https://www.dunnesstoresgrocery.com/"]
