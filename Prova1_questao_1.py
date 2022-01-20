"""
Entrega de trabalho
Eu,

Marcello Gonzatto Birkan 1


declaro que

todas as respostas são fruto do meu próprio trabalho,
não copiei respostas de colegas externos à equipe,
não disponibilizei minhas respostas para colegas externos à equipe e
não realizalizei quaisquer outras atividades desonestas para me beneficiar ou prejudicar outros.
"""


def selectionSort_base(lista):  # Algortimo base cedido pelo professor.
    n = len(lista)
    for preencher_posicao in range(len(lista) - 1, 0, -1):
        indice_maximo = 0
        for localizacao in range(1, preencher_posicao + 1):
            if lista[localizacao] > lista[indice_maximo]:
                indice_maximo = localizacao
        lista[preencher_posicao], lista[indice_maximo] = lista[indice_maximo], lista[preencher_posicao]


def selectionSort(lista):  # Algoritmo modificado especificamente para o exercicio
    for preencher_posicao in range(len(lista)):
        for localizacao in range(preencher_posicao + 1, len(lista)):
            if len(lista[preencher_posicao]) > len(lista[
                                                       localizacao]):  # Ordenação baseada no tamanho da palavra (Numeros de letras que constituem a palavra)
                variavel_axiliar = lista[preencher_posicao]
                lista[preencher_posicao] = lista[localizacao]
                lista[localizacao] = variavel_axiliar
            elif len(lista[localizacao]) == len(lista[
                                                    preencher_posicao]):  # Ordenação alfabetica se, o 'caso' análisado possuir o mesmo numero de letras.
                if lista[localizacao] > lista[preencher_posicao]:
                    variavel_axiliar = lista[localizacao]
                    lista[localizacao] = lista[preencher_posicao]
                    lista[preencher_posicao] = variavel_axiliar
    return lista


def lista_reversa(lista_auxiliar):  # Algoritmo ultilizado para inverter uma lista, uma alternativa ao uso do 'Slicing'=='[::-1]'
    hiindex = len(lista_auxiliar) - 1
    for x in range(len(lista_auxiliar) // 2):
        lista_auxiliar[x], lista_auxiliar[hiindex] = lista_auxiliar[hiindex], lista_auxiliar[x]
        hiindex -= 1


arquivo_palavras = open('palavras_prova.txt', 'r') # Arquivo dispponivel junto ao provaP1.zip
#arquivo_palavras_1 = open('palavras_prova.txt', 'r')
lista_palavras = [] # Lista  ultilizada para auxiliar o processo de ordenação


def metodo_1():
    for x in range(0, 5):  # Leitura exclusiva para as palavras contidas no documento incluido na "PROVA 01".
        linha = (arquivo_palavras.readline().split())
        # lista_palavras.append(linha)
        if x == 0:
            lista_palavras = (linha)
            print(lista_palavras)
            lista_palavras = [x.lower() for x in lista_palavras]
            selectionSort(lista_palavras)
            lista_reversa(lista_palavras)
        elif x == 1:
            lista_palavras1 = (linha)
            print(lista_palavras1)
            lista_palavras1 = [x.lower() for x in lista_palavras1]
            selectionSort(lista_palavras1)
            lista_reversa(lista_palavras1)
        elif x == 2:
            lista_palavras2 = (linha)
            print(lista_palavras2)
            lista_palavras2 = [x.lower() for x in lista_palavras2]
            selectionSort(lista_palavras2)
            lista_reversa(lista_palavras2)
        elif x == 3:
            lista_palavras3 = (linha)
            print(lista_palavras3)
            lista_palavras3 = [x.lower() for x in lista_palavras3]
            selectionSort(lista_palavras3)
            lista_reversa(lista_palavras3)
        elif x == 4:
            lista_palavras4 = (linha)
            print(lista_palavras4)
            lista_palavras4 = [x.lower() for x in lista_palavras4]
            selectionSort(lista_palavras4)
            lista_reversa(lista_palavras4)
    lista_palavras = [lista_palavras, lista_palavras1, lista_palavras2, lista_palavras3, lista_palavras4]
    print(f"-" * 30, "Apos ordenação", f"-" * 30)
    for linhas in lista_palavras:
        print(linhas)
    arquivo_palavras.close()


"""
def metodo_global_teste(lista_palavras): #Não consegui separar por frases, nesse metodo global.
    linha = arquivo_palavras_1.read().split()
    lista_palavras += linha
    print(lista_palavras)
    lista_palavras = [x.lower() for x in lista_palavras]
    selectionSort(lista_palavras)
    lista_reversa(lista_palavras)
    print(lista_palavras)
"""

metodo_1()
#metodo_global_teste(lista_palavras)