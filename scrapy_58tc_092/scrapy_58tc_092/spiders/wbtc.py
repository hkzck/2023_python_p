import scrapy


class WbtcSpider(scrapy.Spider):
    name = "wbtc"
    allowed_domains = ["bj.58.com"]
    start_urls = ["http://bj.58.com/"]

    def parse(self, response):
        #字符串
        # content = response.text
        content = response.body
        print("============================")
        print(content)
        print("============================")
