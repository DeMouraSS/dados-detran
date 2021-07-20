import csv
from unidecode import unidecode
with open('dados-abertos-maio.csv', newline='') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=';')
    for linha in arquivo:
        remover_acentos = unidecode(linha[3].lower())
        print(remover_acentos)
