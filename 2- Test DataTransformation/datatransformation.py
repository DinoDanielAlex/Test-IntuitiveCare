import tabula as tb
import pandas as pd
import zipfile


print("[1] Analisando Documento e coletando as tabelas dos Quadros 30, 31 e 32.")

listtable = tb.read_pdf(".././ComponenteOrganizacional.pdf", pages="108")
listtable31 = tb.read_pdf(".././ComponenteOrganizacional.pdf", pages="109-114")
listtable32 = tb.read_pdf(".././ComponenteOrganizacional.pdf", pages="114")


print("[2]Convertendo as tabelas em extensão .csv")

for table in listtable:
    df = pd.DataFrame(table)
    print("[2.1]Convertendo Quadro 30")
    df.to_csv(".././Quadro_30.csv")
for table in listtable31:
    print("[2.2]Convertendo Quadro 31")
    print("[2.3] Tratando as Tabelas Quadro 31")
    df31 = pd.DataFrame(listtable31[0:6])
    df31.to_csv(".././Quadro_31.csv")
for table in listtable32:
    print("[2.4]Convertendo Quadro 32")
    print("[2.5] Tratando as Tabelas Quadro 32")
    df32 = pd.DataFrame(listtable32[1])
    df32.to_csv(".././Quadro_32.csv")

print("[3]Quadros 30,31,32 extraidos do componente organizacional e salvo na pasta /Tests_IntuitiveCare")

z = zipfile.ZipFile('Teste_Intuitive_Care_Daniel_Alexandre.zip', 'w', zipfile.ZIP_DEFLATED)
print("[4]Comprimindo Quadros em Zip.")
z.write('.././Quadro_30.csv')
z.write('.././Quadro_31.csv')
z.write('.././Quadro_32.csv')
print("[5]Quadros 30, 31 e 32 comprimidos com Sucesso! ")
z.close()

# -////////////////////////////////////////////////////////////////////////////////////////-
# - Code by Daniel Alexandre