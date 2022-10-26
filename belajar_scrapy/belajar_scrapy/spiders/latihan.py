import scrapy

class CobaSpider(scrapy.Spider):
    name = 'fifa_game'
    start_urls = ["https://store.playstation.com/en-id/search/fifa"]
    

    def parse(self, response):
        url = response.url
        
        for i in range(1,5):
            yield scrapy.Request(url=url+str(i), callback=self.parse_details)

    def parse_details(self, response):
        for text in response.css(".psw-product-tile__details"):
            yield{
                "title":text.css(".psw-t-body::text").get(), 
                "price":text.css(".psw-m-r-3::text").get()
            }
        pass

# scrapy crawl fifa_game -t json -o output.json