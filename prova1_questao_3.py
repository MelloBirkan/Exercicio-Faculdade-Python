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
# Todos os algoritmos base de ordenação usados, foram cedidos pelo professor.


def bubbleSort(lista):
    comparacoes = 0
    troca = 0
    indexUltimoElemento = len(lista) - 1
    for passNo in range(indexUltimoElemento, 0, -1):
        for indice in range(indexUltimoElemento):  # Aqui conseguimos "medir" quantas comparações foram feitas
            comparacoes += 1
            if lista[indice] > lista[indice + 1]: # Aqui conseguimos "medir" quantas trocas foram feitas
                troca += 1
                lista[indice], lista[indice + 1] = lista[indice + 1], lista[indice]
    print(f"A) Usando Bubble Sort, foram feitas {comparacoes} comparações e {troca} trocas.")


def insertionSort(lista):
    comparacoes = 0
    troca = 0
    for i in range(1, len(lista)): # Aqui conseguimos "medir" quantas comparações foram feitas
        comparacoes += 1
        j = i - 1
        proximo_elemento = lista[i]
        while (lista[j] > proximo_elemento) and (j >= 0):
            lista[j + 1] = lista[j] # Aqui conseguimos "medir" quantas trocas foram feitas
            troca += 1
            j = j - 1
            lista[j + 1] = proximo_elemento
    return lista and print(f"B) Usando Insertion Sort, foram feitas {comparacoes} comparações e {troca} trocas.")


def selectionSort(lista):
    for preencher_posicao in range(len(lista) - 1, 0, -1):
        indice_maximo = 0
        for localizacao in range(1, preencher_posicao + 1):
            if lista[localizacao] > lista[indice_maximo]:
                indice_maximo = localizacao
        lista[preencher_posicao], lista[indice_maximo] = \
            lista[indice_maximo], lista[preencher_posicao]


def selectionSort_2(lista):
    comparacoes = 0
    troca = 0
    for preencher_posicao in range(len(lista) - 1, 0, -1):
        indice_maximo = 0
        for localizacao in range(1, preencher_posicao + 1): # Aqui conseguimos "medir" quantas comparações foram feitas
            comparacoes+= 1
            if lista[localizacao] > lista[indice_maximo]:
                indice_maximo = localizacao
        lista[preencher_posicao], lista[indice_maximo] = \
            lista[indice_maximo], lista[preencher_posicao] # Aqui conseguimos "medir" quantas trocas foram feitas
        troca+= 1
    print(f"Usando Selection Sort, na ordem decrescente foram feitas {comparacoes} comparações e {troca} trocas.")


def inverter_lista(lista_auxiliar):  #função ultilizada para inverter uma lista, uma alternativa ao uso do 'Slicing'=='[::-1]'
    hiindex = len(lista_auxiliar) - 1
    for x in range(len(lista_auxiliar) // 2):
        lista_auxiliar[x], lista_auxiliar[hiindex] = lista_auxiliar[hiindex], lista_auxiliar[x]
        hiindex -= 1


def separador(n):
    print("-"*n)


def a():
    array = [54,26,93,17,77,31,44,55,20]
    bubbleSort(array)


def b():
    array = [54,26,93,17,77,31,44,55,20]
    insertionSort(array)


def c():
    array = [54,26,93,17,77,31,44,55,20]
    selectionSort(array)
    inverter_lista(array)
    print(f"C) Array invertido: {array}")
    selectionSort_2(array)


a()
separador(70)
b()
separador(70)
c()