import csv
from collections import Counter
from unidecode import unidecode
import os
tipos_veiculos = list()
tipo_arquivo = list()
pasta ='/home/lucas/PycharmProjects/dados-detran1/relatorios'
lista_arquivos = os.listdir(pasta)
arquivos = os.scandir(pasta)
for t in arquivos:
    print(t.name)
print('==' * 50)
with open('relatorios/arquivo(4).csv') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=';')
    for linha in arquivo:
        tipo_veiculo = unidecode(linha[3].lower().strip())
        tipos_veiculos.append(tipo_veiculo)
contador_de_veiculos = Counter(tipos_veiculos)
for chaver, valor in contador_de_veiculos.items():
    print(f"{chaver} - {valor}")
