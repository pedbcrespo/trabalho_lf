def lerArquivo(nome_arquivo):
    dados = {}
    lista_regras = []

    def add_dados(chave, valor, dic=dados):
        dic[chave] = valor

    def dados_lista(linha):
        lista = linha.split()
        return [int(val) for val in lista]

    def def_regras(linha):
        lista = linha.split()
        res = []
        for i in lista:
            val = i
            try:
                val = int(i)
            except:
                pass
            res.append(val)
        return res

    def add_regra(regra, lista_regras=lista_regras):
        lista_regras.append(regra)
        return lista_regras

    lista_comandos = [
        lambda linha: add_dados('num_estados', int(linha)),
        lambda linha: add_dados('num_finais', int(linha)),
        lambda linha: add_dados('estados_finais', dados_lista(linha)),
        lambda linha: add_dados('num_regras', int(linha)),
        lambda linha: add_dados('regras', add_regra(def_regras(linha)))    
    ]

    try:
        with open(nome_arquivo) as arquivo:
            i = 0
            linhas = arquivo.readlines()

            for linha in linhas:
                if i >= 5:
                    lista_comandos[4](linha)
                else:
                    lista_comandos[i](linha)
                i += 1
        
        return dados
    except:
        print("Erro ao abrir o arquivo")
        return False


def gera_grafo(dicionario):
    grafo = []

    for i in range(dicionario['num_estados']):
        grafo.append(['' for i in range(dicionario['num_estados'])])

    for regra in dicionario['regras']:
        pos1 = regra[0]-1
        pos2 = regra[1]-1
        lt = regra[2]
        grafo[pos1][pos2] = lt

    return grafo


# versao recursiva
def verifica_cadeia_alt(dicio, grafo, cadeia, etapa=0): 
    if len(cadeia)==0:
        return etapa+1 in dicio['estados_finais'] 
    else:
        cab = cadeia[0]
        result = False
        for pos in range(len(grafo[etapa])):
            if cab in grafo[etapa][pos]:
                result = result or verifica_cadeia_alt(dicio, grafo, cadeia[1:], pos)
            elif 'e' in grafo[etapa][pos]:
                result = result or verifica_cadeia_alt(dicio, grafo, cadeia, pos)

    return result
