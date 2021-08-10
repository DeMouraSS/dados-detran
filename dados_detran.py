import csv
from collections import Counter
from unidecode import unidecode
tipos_veiculos = list()
with open('dados-abertos-maio.csv') as csvfile:
    arquivo = csv.reader(csvfile, delimiter=';')
    for linha in arquivo:
        tipo_veiculo = unidecode(linha[3].lower().strip())
        tipos_veiculos.append(tipo_veiculo)
contador_de_veiculos = Counter(tipos_veiculos)
for chaver, valor in contador_de_veiculos.items():
    print(f"{chaver} - {valor}")
