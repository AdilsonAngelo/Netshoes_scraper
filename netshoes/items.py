# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class NetshoesItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    nome = scrapy.Field()
    url = scrapy.Field()
    navegacao = scrapy.Field()
    imagem_principal = scrapy.Field()
    imagens_secundarias = scrapy.Field()
    caracteristicas = scrapy.Field()
    descricao = scrapy.Field()
    valor = scrapy.Field()
    valor_antigo = scrapy.Field()

