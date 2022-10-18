import scrapy
from ..helpers import bottle_response


class CellarTestSpider(scrapy.Spider):
    name = 'cellar_test'
    allowed_domains = ['cellar.com']
    start_urls = ['https://cellar.com/wine_vintages/330/2018']

    def parse(self, response):
        counter = 0
        wine_rows = response.css("table#mainContent_gvInventory tr")
        for row in wine_rows:
            if row.css(f"span#mainContent_gvInventory_lblProduct_{counter}").get() == None:
                continue
            bottle = bottle_response(row, counter)
            counter += 1
            yield bottle
    
        if response.css("table#mainContent_gvInventory tr:last-of-type td table"):
            counter_second = 2
            url_base = "https://cellar.com"+response.css("form#Form1::attr(action)").get()
            for link in response.css("table#mainContent_gvInventory tr:last-of-type td table tr td a::attr(href)"):
                data = {
                    '__EVENTTARGET': 'ctl00$mainContent$gvInventory',
                    '__EVENTARGUMENT': f'Page${counter_second}',
                    '__VIEWSTATE': response.css('input[name=__VIEWSTATE]::attr("value")').get(),
                    '__VIEWSTATEGENERATOR': response.css('input[name=__VIEWSTATEGENERATOR]::attr("value")').get(),
                    '__EVENTVALIDATION': response.css('input[name=__EVENTVALIDATION]::attr("value")').get()
                }
                counter_second +=1
                yield scrapy.FormRequest(url=url_base, formdata=data, callback=self.parse_second_page)
                
        
    def parse_second_page(self, response):
        counter = 0
        wine_rows = response.css("table#mainContent_gvInventory tr")
        for row in wine_rows:
            if row.css(f"span#mainContent_gvInventory_lblProduct_{counter}").get() == None:
                continue
            bottle = bottle_response(row, counter)
            counter += 1
            yield bottle


