import json
import shutil
import tempfile

class jsonExp:
    def jsonSave(nome, usuario, ip):
        #Abre o json como arquivo temporário
        with open(R'./Json/est1.json', 'r', encoding='utf-8') as arq, \
            tempfile.NamedTemporaryFile('w', delete=False) as out:
            dados = json.load(arq)

            jsonVerif = False
            num = 1

            #Organiza id por ordem crescente
            for i in dados:

                i['id'] = f"{num}"

                if i['nome'] == nome:
                    jsonVerif = True
                    jsonVerifID = i['id']

                num += 1

            #Salva dados da máquina em um dicionário caso exista a máquina no banco
            if jsonVerif == True:

                dictionary ={ 
                "id" : f"{jsonVerifID}", 
                "nome" : f"{nome}", 
                "usuario" : f"{usuario}", 
                "ip" : f"{ip}"
                } 
                
                dados[int(jsonVerifID)-1] = dictionary

                print(f'Dados do computador {nome} atualizados!')

            #Salva dados da máquina em um dicionário caso não exista a máquina no banco
            else:

                dictionary ={ 
                "id" : f"{len(dados)+1}", 
                "nome" : f"{nome}", 
                "usuario" : f"{usuario}", 
                "ip" : f"{ip}"
                }
                dados.append(dictionary) 

                print(f'Computador {nome} inserido!')

            #Salva o Json temporário
            json.dump(dados, out, ensure_ascii=False, indent=4, separators=(',',':'))
        #Substitui o original
        shutil.move(out.name, R'./Json/est1.json')
        