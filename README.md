# Teste Prático em Scrapy

##1.Descrição
Esse projeto consiste do desenvolvimento de um scraper para obtenção de informações de produtos em sites de vendas on line. Para isso foi utilizada a ferramenta **Scrapy** e o banco de dados **MongoDB**. Como target foi escolhido o site de vendas de produtos esportivos  [Netshoes](https://www.netshoes.com.br/) do qual foram extraídas os seguinte atributos:


*    **nome:** 
*    **URL:**  
*    **navegacao:**
*    **imagem_principal:**
*    **imagens_secundarias:**
*    **caracteristicas:**
*    **descricao:**
*    **valor:**
*    **valor_antigo:**


##2.Execução
Para a execução são necessárias as seguintes etapas
###2.1Scrapy 
Instalação:



```
pip install scrapy
```



###2.2Mongodb
Instalação:
```
pip install pymongo
```

Inicialização do servidor:
```
mongod
```
###2.3Visualização dos Dados
Para melhor visualização dos dados é recomendado o uso do software [Robo3T](https://robomongo.org). O mesmo deve ser instalado e ao abrir seu executável deve-se criar uma conexão com o servidor criado na seção 2.2

###2.4Execução do Projeto 
Para a execução do projeto é necessário o download do repositório através do comando

```git clone https://github.com/larifeliciana/Netshoes_scraper```

No diretório Netshoes_scraper deve-se executar o seguinte comando para entrar no diretório principal do projeto

   ``` cd netshoes ```
   
   
   
 E para a execução da Spider:
 
 ```scrapy runspider netshoes/spiders/Netshoes.py -a search_string="camiseta"```
 



A váriavel search_string pode ser trocada pelo produto que se deseja buscar.

Após esse comando os dados começaram a ser armazenados no servidor MongoDB e pode ser visualizado do Robo3t

##Detalhes sobre o desenvolvimento

Para o desenvolvimento desse projeto foram utilizados:



* 30 minutos para instalação de ferramentas
* 1 hora de estudo das ferramentas a serem utilizadas
* 1 hora para escolha e estudo do target
* 3 horas para o desenvolvimento 
* 1 hora para solução de bugs
