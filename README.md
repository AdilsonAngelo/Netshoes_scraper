# Teste Prático em Scrapy

## 1 Descrição
Esse projeto consiste do desenvolvimento de um scraper para obtenção de informações de produtos em sites de vendas on line. Para isso foi utilizada a ferramenta **Scrapy** e o banco de dados **MongoDB**. Como target foi escolhido o site de vendas de produtos esportivos  [Netshoes](https://www.netshoes.com.br/) do qual foram extraídas os seguinte atributos:


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
Para a execução são necessárias as seguintes etapas

### 2.1 Instalação Scrapy 




```
pip install scrapy
```


 
### 2.2 Instalação Mongodb e pymongo
 O MondoDB pode ser baixo e instalado no site [MongoDB](https://www.mongodb.com/download-center/community) ou através dos seguintes comandos no terminal linux:
 
```sudo apt-key adv –keyserver hkp://keyserver.ubuntu.com:80 –recv 7F0CEB10```

```echo “deb http://repo.mongodb.org/apt/ubuntu trusty/mongodb-org/3.0 multiverse” | sudo tee /etc/apt/sources.list.d/mongodb-org-3.0.lis ```
```sudo apt-get update```

```apt-get install mongodb-org```


É necessário também a criação dos diretórios data/db na raiz do sistema. Após a instalação o serviço pode ser inicializado com o seguinte comando:
```
mongod
```
ou 

```sudo service mongod start```

Para a instalação do pymongo se insere o seguinte comando:
```
pip install pymongo
```

### 2.3 Visualização dos Dados
Para melhor visualização dos dados é recomendado o uso do software [Robo3T](https://robomongo.org). O mesmo deve ser instalado e ao abrir seu executável conectar-se com o servidor criado na seção 2.2. No site está disponível download tanto para Linux quando Windows. Os dados extrado do site podero ser visualizados no banco **netshoesdb** na coleção **produtos**. 

### 2.4 Execução do Projeto 
Para a execução do projeto é necessário o download do repositório através do comando

```git clone https://github.com/larifeliciana/Netshoes_scraper```

No diretório Netshoes_scraper deve-se executar o seguinte comando para execução do projeto
  ```cd Netshoes_scraper```
   
 E para a execução da Spider:
 
 ```scrapy runspider netshoes/spiders/Netshoes.py -a search_string="camiseta"```
 



A váriavel search_string pode ser trocada pelo produto que se deseja buscar.

Após esse comando os dados começaram a ser armazenados no servidor MongoDB e pode ser visualizado do Robo3t

## 3 Detalhes sobre o desenvolvimento

Para o desenvolvimento desse projeto foram utilizados:


* 1/2 hora para instalação de ferramentas
* 1 hora de estudo das ferramentas a serem utilizadas
* 1 hora para escolha e estudo do target
* 3 horas para o desenvolvimento 
* 1 hora para solução de bugs

Não foi necessário o uso de manipulação de querystrings e chamadas assícronas.

