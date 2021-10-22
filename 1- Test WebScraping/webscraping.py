import os
from bs4 import BeautifulSoup
import requests
from requests.models import Response

print("[1] Site que será coletado")
site = "https://www.gov.br/ans/pt-br/assuntos/prestadores/padrao-para-troca-de-informacao-de-saude-suplementar-2013-tiss"
print(site)

print("[2] Coletando os dados do site")
html = requests.get(site).content

print("[3] Formatando os dados")
dados = BeautifulSoup(html, 'html.parser')

print("[4] Buscando por classe")
busca_por_class = dados.find('p', attrs={'class': 'callout'})

print("[5] Coletando a tag dentro da div")
extensao = busca_por_class.find("a")

print("[6] Adicionando a Extensao no Link")
sitelink = (extensao.attrs['href'])

print("[7] Procurando por ultimo Componente Organizacional")
htmlpdf = requests.get(sitelink).content
dadospdf = BeautifulSoup(htmlpdf, 'html.parser')
busca_por_classpdf = dadospdf.find("div", class_="table-responsive")
extensaopdf = busca_por_classpdf.find("a")
sitepdf = (extensaopdf.attrs['href'])

print("[8] Link do pdf encontrado e alinhado para download")

print(sitepdf)

print("[9] Fazendo Download do PDF")
pdf = requests.get(sitepdf).content
def baixar_arquivo(url, endereco):
    resposta = requests.get(url)
    if resposta.status_code == requests.codes.OK:
        with open (endereco, 'wb') as novo_arquivo:
            novo_arquivo.write(resposta.content)
        print("[10] Download finalizado. Salvo em: {}".format(endereco))
    else:
        resposta.raise_for_status()
if __name__ == '__main__':
    baixar_arquivo(sitepdf, '.././ComponenteOrganizacional.pdf')
print("Salvo em: ./Tests_IntuitiveCare/1- Test WebScraping")
