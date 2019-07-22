from pymongo import MongoClient
import pandas as pd
from pprint import pprint
from sklearn.feature_extraction.text import CountVectorizer

# no bd consta os seguintes documentos por marca:
# 1-758 adidas
# 759-763 puma
# 764-2109 mizuno


class Netshoes(object):
    def __init__(self):
        self.dataframe = None
        self.client = MongoClient('localhost', 27018)
        self.produtos = [
            {
                'valor': prod['valor'],
                'genero': None if 'Gênero:' not in prod['caracteristicas']
                else prod['caracteristicas']['Gênero:'],
                'descricao': prod['descricao']
            } for prod in self.client.netshoesdb.produtos.find()]

    def get_adidas(self):
        adidas = self.produtos[:757]
        for item in adidas:
            item.update({'query': 'adidas'})
        return adidas

    def get_puma(self):
        puma = self.produtos[758:762]
        for item in puma:
            item.update({'query': 'puma'})
        return puma

    def get_mizuno(self):
        mizuno = self.produtos[763:]
        for item in mizuno:
            item.update({'query': 'mizuno'})
        return mizuno

    def setup_dataframe(self):
        self.dataframe = pd.DataFrame(
            self.get_adidas() + self.get_puma() + self.get_mizuno())

    def get_N_most_frequent(self, n, brand='adidas'):
        if self.dataframe is None:
            self.setup_dataframe()
        corpus = self.dataframe[self.dataframe['query']
                                == brand].descricao.dropna()
        words_freq = self.get_words_freq(corpus)
        return words_freq[:n]

    def get_words_freq(self, corpus):
        vec = CountVectorizer().fit(corpus)
        bag_of_words = vec.transform(corpus)
        sum_words = bag_of_words.sum(axis=0)
        words_freq = [(word, sum_words[0, idx])
                      for word, idx in vec.vocabulary_.items()]
        words_freq = sorted(words_freq, key=lambda x: x[1], reverse=True)
        return words_freq

    def generate_report(self):
        if self.dataframe is None:
            self.setup_dataframe()
        with open('report.json', 'w') as report:
            import json
            obj = []
            for brand in ['adidas', 'puma', 'mizuno']:
                data = dict()
                data['brand'] = brand
                df = self.dataframe.dropna()
                df = df[df['query'] == brand]
                data['word_freq'] = dict()
                for word, freq in self.get_N_most_frequent(10, brand):
                    data['word_freq'][word] = int(freq)
                data['gender'] = dict()
                for index, value in df['genero'].value_counts().iteritems():
                    data['gender'][index.strip()] = value
                data['min_value'] = df['valor'].min()
                data['max_value'] = df['valor'].max()
                obj.append(data)
            json.dump(obj, report, ensure_ascii=False)
        print('report generated!')


if __name__ == "__main__":
    netshoes = Netshoes()

    # pprint(netshoes.get_N_most_frequent(10))
    netshoes.generate_report()
    # report = open('report.txt', 'w')
    # report.write(pprint(words_freq))
    # report.close()
