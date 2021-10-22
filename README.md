# Teste IntuitiveCare



<H1>Olá caros leitores, neste repositório está meus testes para a Empresa IntuitiveCare.</H1>

<H3>Testes:</H3>

<h6>Web Scraping



<h6>Data Transformation



<h6>Data Base



<h6>Front-end





<H2>LEIA-ME</H2>
instalar as bibliotecas:

* pip install beautifulsoup4
* pip install requests
* pip install tabula-py
* pip install pandas

* Java 8+

<h3>Inicie pelo Test Web Scrapping para que seja criado o arquivo Componente Organizacional que vai ser usado no Teste 2.</h3>

Para rodar os arquivos basta entrar na pasta do Teste 1 Web Scraping clicar com botão direito do mouse

abrir o terminal do windows  e digitar python webscraping.py

e o mesmo deve fazer para rodar o Teste 2 

certifique-se de ter baixado as bibliotecas sinalizadas acima

Depois de rodar os Arquivos ".py" dê [F5] na página para visualizar os arquivos novos.





Test Web Scrapping

* Usei Python para fazer o WebScraping com a biblioteca BeautifulSoup4 e Requests;

Test Data Transformation

* Usei Python para fazer a extração das tabelas do arquivo Componente Organizacional;
  Utilizei o tabula para pegar apenas as páginas que irei usar e separei os quadros com o pandas em dataframes, fiz o tratamento pois a ultima página continha dados de 2 grupos distintos.
* Feito isso consegui a extração e conversão para os Quadros 30, 31 e 32 em .csv 
* Usei a Biblioteca Zipfile para comprimir em .zip 
  Como não tinha nada escrito que precisaria excluir o .csv após a compressão eu deixei ele.

Test Data Base

