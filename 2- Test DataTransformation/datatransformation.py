import tabula as tb
import pandas as pd
import zipfile
print("[1] Analisando Documento e coletando as tabelas dos Quadros 30, 31 e 32.")
listtable = tb.read_pdf("../1- Test WebScraping/ComponenteOrganizacional.pdf", pages="108,109-113,114")
print("[2]Convertendo as tabelas em extensão .csv")
df = pd.DataFrame(listtable)
df.to_csv("Quadros303132.csv")
print("[3]Quadros 30,31,32 extraidos do componente organizacional e salvo na pasta /Tests_IntuitiveCare")
z = zipfile.ZipFile('Quadros303132.zip', 'w', zipfile.ZIP_DEFLATED)
print("[4]Comprimindo Quadros303132 em Zip.")
z.write('Quadros303132.csv')
print("[5]Quadros 30, 31 e 32 comprimidos com sucesso! ")
z.close()
# Código antigo que não consegui fazer a conversão para+ .csv por problemas no encoding
'''
Quadro30 = tb.convert_into("ComponenteOrganizacional.pdf", "Quadro30.csv", output_format="csv", pages='108')
Quadro31 = tb.convert_into("ComponenteOrganizacional.pdf", "Quadro31.csv", output_format="csv", pages='109-113')
Quadro32 = tb.convert_into("ComponenteOrganizacional.pdf", "Quadro32.csv", output_format="csv", pages='114')
'''
