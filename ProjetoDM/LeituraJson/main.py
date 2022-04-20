from xlsx import expXlsx
from jsonVerif import jsonVerif
import json

jsonV = jsonVerif
expX = expXlsx

#Abre o json e salva dentro de uma variável
with open(R'./Json/est1.json', encoding='utf-8') as meu_json:
    dados = json.load(meu_json)
    #Ordena as máquinas por ordem crescente
    jsonV.jsonOrder()

#Salva os dados na planilha
for i in dados:
    expX.export(i['id'], i['nome'], i['usuario'], i['ip'])

print('Tabela atualizada com sucesso!')