

import scrapy
from powerPlant.items import PowerplantItem

class PowerSpider(scrapy.Spider):
    name = "plant_spider"
    start_urls = ['https://sitr.cnd.com.pa/m/pub/vert.html']

    def parse(self, response):

            item = PowerplantItem()
            for row in response.xpath(
                    '//table[@class="table table-hover table-striped table-sm table-bordered sitr-table-embalse"]'):
                for row1 in row.xpath('./tbody/tr'):
                    item['planta'] = row1.xpath('./td[3]/span/text()').get()
                    item['potencia'] = row1.xpath('./td[7]/span/text()').get()
                    item['porcentaje'] = row1.xpath('./td[8]/div/div/span/text()').get()
                    item['tipo'] = 'Hidroelectricas'
                    yield item

            for row in response.xpath('//table[@id="solar"]'):
                for row1 in row.xpath('./tbody/tr'):
                    item['planta'] = row1.xpath('./td[2]/span/text()').get()
                    item['potencia'] = row1.xpath('./td[4]/span/text()').get()
                    item['porcentaje'] = row1.xpath('./td[5]/div/div/span/text()').get()
                    item['tipo'] = 'Solares'
                    yield  item

            for row in response.xpath('//table[@id="eolica"]'):
                for row1 in row.xpath('./tbody/tr'):
                    item['planta'] = row1.xpath('./td[2]/span/text()').get()
                    item['potencia'] = row1.xpath('./td[4]/span/text()').get()
                    item['porcentaje'] = row1.xpath('./td[5]/div/div/span/text()').get()
                    item['tipo'] = 'Eolicas'
                    yield item



