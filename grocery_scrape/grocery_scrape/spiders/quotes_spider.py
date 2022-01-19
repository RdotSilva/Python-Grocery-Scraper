import scrapy


class QuotesSpider(scrapy.Spider):
    """Example class used for reference"""

    # Identifies the spider. It must be unique within a project, that is, you can’t set the same name for different Spiders
    name = "quotes"

    # Use start_urls instead of using the start_requests (think of this as a shortcut)
    start_urls = [
        "http://quotes.toscrape.com/page/1/",
        "http://quotes.toscrape.com/page/2/",
    ]

    # Commented out because we are using start_urls above
    # def start_requests(self):
    #     """must return an iterable of Requests (you can return a list of requests or write a generator function) which the Spider will begin to crawl from. Subsequent requests will be generated successively from these initial requests."""
    #     urls = [
    #         "http://quotes.toscrape.com/page/1/",
    #         "http://quotes.toscrape.com/page/2/",
    #     ]
    #     for url in urls:
    #         yield scrapy.Request(url=url, callback=self.parse)

    # Parse is scrapy's default callback
    def parse(self, response):
        """Method that will be called to handle the response downloaded for each of the requests made. The response parameter is an instance of TextResponse that holds the page content and has further helpful methods to handle it."""
        page = response.url.split("/")[-2]
        filename = f"quotes-{page}.html"
        with open(filename, "wb") as f:
            f.write(response.body)
        self.log(f"Saved file {filename}")
