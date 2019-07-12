# -*- coding: utf-8 -*-
import scrapy
from netshoes.items import NetshoesItem
import logging
class NetshoesSpider(scrapy.Spider):
    name = 'Netshoes'
    allowed_domains = ['www.netshoes.com.br']
    start_urls = ['http://www.netshoes.com.br/']
    i = 0
  
    def parse(self, response):

        logging.info('\n## Inicio parse \n\n\n')
        logging.info('## Iniciando o acesso ao site: %s em busca do produto %s ' % (response.url, self.search_string))


        yield scrapy.FormRequest.from_response(response, formdata={"q": self.search_string,
                                                                   }, callback=self.scrape_search_page,
                                               dont_filter=True, formxpath="//form[@class=\"wrapper search-form\"]")



    def scrape_search_page(self, response):

        logging.info('## Obtendo produtos da página de busca de numéro '+str(self.i)+"\n")
        self.i = self.i + 1

        link_produtos = response.xpath("//a[@class=\"i card-link\"]/@href").extract()

        for i in link_produtos:
            yield scrapy.Request("https://"+i, self.scrape_product_page, dont_filter=True)


        try:

            next_page = "http://"+response.xpath("//span[@class=\"selected\"]/following-sibling::a/@href").extract_first()
            open("text.txt","a").write(next_page)
            yield scrapy.Request(next_page, self.scrape_search_page, dont_filter=True)

        except:
            logging.info('## Página final alcançada')



    def scrape_product_page(self, response):

        produto = NetshoesItem()

        produto["nome"] = response.xpath("//h1[@itemprop=\"name\"]/text()").extract_first()

        produto["url"] = response.url

        produto["descricao"] = response.xpath("//p[@itemprop=\"description\"]/text()").extract_first()



        produto["imagem_principal"] =  response.xpath("//figure[@class=\"photo-figure\"]/img/@src").extract_first()

        produto["imagens_secundarias"] = response.xpath("//ul[@class=\"swiper-wrapper\"]/li/figure/img/@src").extract()




        produto["valor"] = float(response.xpath("//strong[@itemprop=\"price\"]/text()").extract_first().split(' ')[1].replace(".","").replace(",","."))


        try:
            produto["valor_antigo"] = float(response.xpath("//del[@class=\"default-price reduce \"]/text()").extract_first().split(' ')[1].replace(".","").replace(".","").replace(",","."))
        except:
            produto["valor_antigo"] = produto["valor"]


        produto["navegacao"] = response.xpath("//li[@itemprop=\"itemListElement\"]/a/span/text()").extract()




        caracteristicas = {}

        key = response.xpath("//ul[@class=\"attributes\"]/li/strong/text()").extract()
        value = response.xpath("//ul[@class=\"attributes\"]/li/text()").extract()


        for k,v in zip(key, value):
            caracteristicas.update({k:v})

        produto["caracteristicas"] = caracteristicas

        yield produto
