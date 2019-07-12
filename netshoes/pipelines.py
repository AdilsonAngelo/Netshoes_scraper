# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymongo
import logging
class NetshoesPipeline(object):

    def open_spider(self, spider):

        logging.info('\n\n## Abrindo conexao com o banco...\n\n')

        self.conexao = pymongo.MongoClient("mongodb://localhost:27017/")
        base = self.conexao["netshoesdb"]
        self.colecao = base["produtos"]

    def close_spider(self, spider):

        self.conexao.close()
        logging.info('\n\n## Fechando conexao com o banco... \n\n')

    def process_item(self, item, spider):

        if len([i for i in self.colecao.find({"url": item["url"]})]) < 1:  # Checa se item não já foi adicionado através do url
            self.colecao.insert(dict(item))

        else:
            logging.info('## O produto a ser inserido ja foi adicionado anteriormente. roduto: %s', item["nome"])

        return item