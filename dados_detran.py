import csv
from collections import Counter
from unidecode import unidecode
import os
tipos_veiculos = list()
tipos_infracoes = list()
tipo_arquivo = list()
pasta ='/home/lucas/PycharmProjects/dados-detran1/relatorios'
lista_arquivos = os.listdir(pasta)
arquivos = os.scandir(pasta)
for t in arquivos:
    print(t.name)
print('==' * 50)
with open('relatorios/arquivo(3).csv') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=';')
    for linha in arquivo:
        tipo_infracao = linha[12]
        tipo_veiculo = unidecode(linha[3].lower().strip())
        tipos_veiculos.append(tipo_veiculo)
        tipos_infracoes.append(tipo_infracao)
contador_de_veiculos = Counter(tipos_veiculos)
contador_de_infracoes = Counter(tipos_infracoes)
for chaver, valor in contador_de_veiculos.items():
    print(f"{chaver} - {valor}")
print('~' * 50)
for coluna, v in contador_de_infracoes.items():
    print(f"{coluna} - {v}")
