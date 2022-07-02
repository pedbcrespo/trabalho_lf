import afnd

if __name__ == '__main__':
    # dicio = afnd.lerArquivo('teste.txt')    
    # grafo = afnd.gera_grafo(dicio)
    # print(grafo)
    # cadeia = "ba"
    # print(afnd.verifica_cadeia(dicio, grafo, cadeia))

    while True:
        
        op = int(input("1-Verificar cadeia:\n2-Sair\n"))
        if op==1:
            nomeArq=input("Arquivo texto: ")
            infoArq=afnd.lerArquivo(nomeArq)
            grafo = afnd.gera_grafo(infoArq)
            print(grafo)
            cadeia=input("Digite a cadeia: ")
            print(afnd.verifica_cadeia_alt(infoArq, grafo, cadeia))
                        
        elif op==2:
            print("Saindo...")
            break
        else:
            op = input("Opcao invalida, digite novamente: ")

