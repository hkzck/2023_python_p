import scrapy


class BaiduSpider(scrapy.Spider):
    #运行爬虫得时候用
    name = "baidu"
    #具体爬得时候要用到得网址
    allowed_domains = ["www.baidu.com"]
    #起始url,第一次要访问得
    start_urls = ["http://www.baidu.com/"]


    def parse(self, response):
        print(111)
