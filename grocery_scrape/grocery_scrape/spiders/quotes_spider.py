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
        for quote in response.css("div.quote"):
            yield {
                "text": quote.css("span.text::text").get(),
                "author": quote.css("small.author::text").get(),
                "tags": quote.css("div.tags a.tag::text").getall(),
            }

        # Crawl through all pages
        next_page = response.css("li.next a::attr(href)").get()
        if next_page is not None:
            next_page = response.urljoin(next_page)
            yield response.follow(next_page, callback=self.parse)
