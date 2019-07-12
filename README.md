# Teste Prático em Scrapy

## 1 Descrição
Este projeto apresenta um scraper para obtenção de informações de produtos em sites de vendas on-line. Para isso, foi utilizada a ferramenta **Scrapy** e o banco de dados **MongoDB**. Como target, foi escolhido o site de vendas de produtos esportivos [Netshoes](https://www.netshoes.com.br/), do qual foram extraídos os seguintes atributos:


*    **nome** 
*    **URL**  
*    **navegacao**
*    **imagem_principal**
*    **imagens_secundarias**
*    **caracteristicas**
*    **descricao**
*    **valor**
*    **valor_antigo**


## 2 Execução
Para a execução, são necessárias as etapas abaixo.

### 2.1 Instalação Scrapy 




```
pip install scrapy
```


 
### 2.2 Instalação MongoDB e PyMongo
 O **MondoDB** pode ser baixo e instalado no site [MongoDB](https://www.mongodb.com/download-center/community), ou através dos seguintes comandos no terminal Linux:
 
```sudo apt-key adv –keyserver hkp://keyserver.ubuntu.com:80 –recv 7F0CEB10```

```echo “deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse” | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.lis ```
```sudo apt-get update```

```apt-get install mongodb-org```


É necessária também a criação do diretório **db** em um diretório **data** na raiz do sistema. Após a instalação, o serviço pode ser inicializado com o seguinte comando:
```
mongod
```
ou também pelo comando

```sudo service mongod start```

Para a instalação do PyMongo, o comando abaixo deve ser usado:
```
pip install pymongo
```

### 2.3 Visualização dos Dados
Para melhor visualização dos dados, é recomendado o uso do software [Robo3T](https://robomongo.org). O usuário deverá abrir seu arquivo executável e conectar-se ao serviço criado na seção 2.2. O software *Robo3T* está disponível no site, estando disponível tanto para o sistema operacional Linux, quanto para o Windows. Os dados extrado do site poderão ser visualizados no banco **netshoesdb** na coleção **produtos**. 

### 2.4 Execução do Projeto 
Para a execução do projeto, é necessário o download de seu repositório através do comando

```git clone https://github.com/larifeliciana/Netshoes_scraper```

É necessária a execução do comando

  ```cd Netshoes_scraper```
   
para ter acesso ao projeto e para a execução do *Spider*:
 
 ```scrapy runspider netshoes/spiders/Netshoes.py -a search_string="camiseta"```
 



A váriavel *search_string* pode ser trocada pelo produto que se deseja buscar.

Após esse comando, os dados começaram a ser armazenados no servidor MongoDB, e podem ser visualizados no Robo3T.

## 3 Detalhes sobre o Desenvolvimento

Para o desenvolvimento deste projeto, foram utilizados:


* 1/2 hora para instalação de ferramentas;
* 1 hora de estudo das ferramentas a serem utilizadas;
* 1 hora para escolha e estudo do target;
* 4 horas para o desenvolvimento; 
* 1 hora para solução de bugs.

Não foi necessário o uso de manipulação de *querystrings* e chamadas assícronas.

