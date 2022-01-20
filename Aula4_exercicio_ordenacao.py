from random import randint
import time
import matplotlib.pyplot as plt
import numpy as np

# gere dados aleatórios (10, 100, 500, 1000, 5000, 10000) e salve-os em arquivos.
# abra os arquivos, leia-os, carregue os valores em listas e ordene-as com os algoritmos bubble, insertion e selection.
# realize a aferição temporal de cada ordenação.
# plote os gráficos pertinentes para comparação dos tempos de execução.
arquivo0 = []
arquivo1 = []
arquivo2 = []
arquivo3 = []
arquivo4 = []
vetores = [10, 100, 500, 1000, 5000, 1000]
for x in range(5):
    arquivos = open(r"C:\Users\Pichau\iCloudDrive\Faculdade\Segundo "
                    r"Semestre\Python\Lab_Algortimos_e_Programacao_II\Exercicio "
                    r"entregas\Aula_4_exercicio/arquivo" + str(x) + ".txt", "w")
    for z in range(vetores[x]):
        arquivos.write(f"\n{str(randint(1, 10000))}\n")
    arquivos.close()


def abrir(arquivo, arquivo_append):
    abrir_arquivos = open(arquivo, "r")
    for c in abrir_arquivos:
        linha = abrir_arquivos.readline().rstrip('\n')
        arquivo_append.append(linha)


def bubbleSort(lista):
    indexUltimoElemento = len(lista)-1
    for passNo in range(indexUltimoElemento, 0, -1):
        for indice in range(indexUltimoElemento):
            if lista[indice]>lista[indice+1]:
                lista[indice],lista[indice+1]=lista[indice+1],lista[indice]


def insertionSort(lista):
    for i in range(1, len(lista)):
        j = i-1
        proximo_elemento = lista[i]
        while (lista[j] > proximo_elemento) and (j >= 0):
            lista[j+1] = lista[j]
            j=j-1
            lista[j+1] = proximo_elemento
    return lista


def selectionSort(lista):
    for preencher_posicao in range(len(lista) - 1, 0, -1):
        indice_maximo = 0
        for localizacao in range(1, preencher_posicao + 1):
            if lista[localizacao] > lista[indice_maximo]:
                indice_maximo = localizacao
        lista[preencher_posicao],lista[indice_maximo]=\
            lista[indice_maximo],lista[preencher_posicao]


abrir(r"C:\Users\Pichau\iCloudDrive\Faculdade\Segundo "
                        r"Semestre\Python\Lab_Algortimos_e_Programacao_II\Exercicio "
                        r"entregas\Aula_4_exercicio/arquivo0.txt", arquivo0)
abrir(r"C:\Users\Pichau\iCloudDrive\Faculdade\Segundo "
                        r"Semestre\Python\Lab_Algortimos_e_Programacao_II\Exercicio "
                        r"entregas\Aula_4_exercicio/arquivo1.txt", arquivo1)
abrir(r"C:\Users\Pichau\iCloudDrive\Faculdade\Segundo "
                        r"Semestre\Python\Lab_Algortimos_e_Programacao_II\Exercicio "
                        r"entregas\Aula_4_exercicio/arquivo2.txt", arquivo2)
abrir(r"C:\Users\Pichau\iCloudDrive\Faculdade\Segundo "
                        r"Semestre\Python\Lab_Algortimos_e_Programacao_II\Exercicio "
                        r"entregas\Aula_4_exercicio/arquivo3.txt", arquivo3)
abrir(r"C:\Users\Pichau\iCloudDrive\Faculdade\Segundo "
                        r"Semestre\Python\Lab_Algortimos_e_Programacao_II\Exercicio "
                        r"entregas\Aula_4_exercicio/arquivo4.txt", arquivo4)


lista_bubble = lista_insertion = lista_selection = arquivo0 + arquivo2 + arquivo1 + arquivo3 + arquivo4



inicio_i = time.time()
insertionSort(lista_insertion)
fim_i = time.time()
tempo_insertion = fim_i  - inicio_i
print(f"demorou {tempo_insertion:.2f} segundos para ordenar em InsertionSort")


inicio_b= time.time()
bubbleSort(lista_bubble)
fim_b= time.time()
tempoBubble = fim_b -inicio_b
print(f"demorou {tempoBubble:.2f} segundos para ordenar em BubbleSort")

inicio_s = time.time()
selectionSort(lista_selection)
fim_s = time.time()
tempo_selection = fim_s - inicio_s
print(f"demorou {tempo_selection:.2f} segundos em média para ordenar em SelectionSort")


Sortts = ['BubbleSort','Insertion','Selection']
tempos = [tempoBubble,tempo_insertion,tempo_selection]

plt.figure(figsize=(12,8))

x = np.arange(len(Sortts))

plt.bar(x,tempos, width = 0.5, color='firebrick')

plt.xticks([x for x in range(len(Sortts))], Sortts)

plt.yticks(np.arange(0, 4, 0.25))

plt.grid(True)

plt.figtext(.515,.9,'Tempos para ordenar em Python usando os segunites algoritmos\nMenos melhor', fontsize=20, ha='center')

plt.xlabel('Algoritmos',fontsize=18)

plt.ylabel('Tempo em segundos',fontsize=18)

plt.show()
