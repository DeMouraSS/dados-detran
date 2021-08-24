import csv
from collections import Counter
from unidecode import unidecode
import os
from openpyxl import Workbook
arquivo_excel = Workbook()
tipos_veiculos = list()
tipos_infracoes = list()
tipo_arquivo = list()
contador = 1
pasta ='/Users/aman.rathie/PycharmProjects/detrans/relatorios'
lista_arquivos = os.listdir(pasta)
arquivos = os.scandir(pasta)
for t in arquivos:
    print(t.name)
    print('==' * 50)
    nome_arquivo = 'relatorios/' + t.name
    with open(nome_arquivo) as csvfile:
        arquivo = csv.reader(csvfile, delimiter=';')
        for linha in arquivo:
            tipo_infracao = linha[12]
            tipo_veiculo = unidecode(linha[3].lower().strip())
            tipos_veiculos.append(tipo_veiculo)
            tipos_infracoes.append(tipo_infracao)
    contador_de_veiculos = Counter(tipos_veiculos)
    contador_de_infracoes = Counter(tipos_infracoes)
    #del contador_de_veiculos['tipo_veiculo']
    planilha1 = arquivo_excel.create_sheet(t.name)
    for tipo_v, valor in contador_de_veiculos.items():
        print(f"{tipo_v} - {valor}")
        contador += 1
        planilha1.cell(row=contador, column=1, value=tipo_v)
        planilha1.cell(row=contador, column=2, value=valor)
    print('~' * 50)
    for coluna, v in contador_de_infracoes.items():
        print(f"{coluna} - {v}")
arquivo_excel.save("relatorio.xlsx")