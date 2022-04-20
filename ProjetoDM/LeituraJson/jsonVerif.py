import json
import shutil
import tempfile

class jsonVerif:
    def jsonOrder():
        #Abre o json como arquivo temporário
        with open(R'./Json/est1.json', 'r', encoding='utf-8') as arq, \
            tempfile.NamedTemporaryFile('w', delete=False) as out:
            dados = json.load(arq)
            arrayNum = []
            nameNum = ""
            aux = ""

            #Separa o número de identificação no nome da máquina do pré-fixo
            for i in dados:
                nameNum = ""
                for ch in i['nome']:
                    if ch.isdigit():
                        nameNum += ch
                arrayNum.append(nameNum)

            arrayNum.sort()
        
            #Ordena as máquinas por ordem crescente, usando o nome como critério
            for i in range(len(arrayNum)):
                for j in range(len(arrayNum)):
                    if dados[j]['nome'] == f'E-EST{i}':
                        aux = dados[j]
                        dados[j] = dados[i]
                        dados[i] = aux
                        dados[i]['id'] = f"{i-1}" 

            #Salva o Json temporário
            json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))
        #Substitui o original
        shutil.move(out.name, R'./Json/est1.json')

            

            
            




