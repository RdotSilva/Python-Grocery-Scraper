import scrapy


class GrocerySpider(scrapy.Spider):
    """Class to crawl Grocery pages"""

    name = "grocery"

    start_urls = ["https://www.dunnesstoresgrocery.com/"]

    def parse(self, response):
        for item in response.css('div[data-testid="productListingShoppingRuleWrapper"]').extract() 
            yield {
                'text': item.css('div.text::text').get(),

            }