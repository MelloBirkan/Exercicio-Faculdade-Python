import random
import time


def buscaBinaria(lista, item):
    primeiro = 0
    ultimo = len(lista) - 1
    encontrado = False
    contador_de_comp = 0
    while primeiro <= ultimo and not encontrado:
        meio = (primeiro + ultimo) // 2
        if lista[meio] == item:
            encontrado = True
        else:
            if item < lista[meio]:
                ultimo = meio - 1
            else:
                primeiro = meio + 1
    return encontrado


def selectionSort(lista):
    for preencher_posicao in range(len(lista) - 1, 0, -1):
        indice_maximo = 0
        for localizacao in range(1, preencher_posicao + 1):
            if lista[localizacao] > lista[indice_maximo]:
                indice_maximo = localizacao
        lista[preencher_posicao], lista[indice_maximo] = \
            lista[indice_maximo], lista[preencher_posicao]



lista10 = []
for x in range(10):
    lista10.append(random.randint(1, 10))
selectionSort(lista10)
lista100 = []
for x in range(10):
    lista100.append(random.randint(1, 100))
selectionSort(lista100)
lista1000 = []
for x in range(10):
    lista1000.append(random.randint(1, 1000))
selectionSort(lista1000)
lista10000 = []
for x in range(10):
    lista10000.append(random.randint(1, 100000))
selectionSort(lista10000)
lista100000 = []
for x in range(10):
    lista10000.append(random.randint(1, 1000000))
selectionSort(lista100000)

inicio_a = time.time()
print(buscaBinaria(lista10, random.randint(1,10)))
fim_a= time.time()
tempolista10 = fim_a -inicio_a
print(f"Demorou {tempolista10:.2f} segundos para fazer a busca numa lista de 10 itens")

inicio_a = time.time()
print(buscaBinaria(lista100,random.randint(1,100)))
fim_a= time.time()
tempolista10 = fim_a -inicio_a
print(f"Demorou {tempolista10:.2f} segundos para fazer a busca numa lista de 100 itens")

inicio_a = time.time()
print(buscaBinaria(lista1000,random.randint(1,1000)))
fim_a= time.time()
tempolista10 = fim_a -inicio_a
print(f"Demorou {tempolista10:.2f} segundos para fazer a busca numa lista de 1000 itens")

inicio_a = time.time()
print(buscaBinaria(lista10000,random.randint(1,10000)))
fim_a= time.time()
tempolista10 = fim_a -inicio_a
print(f"Demorou {tempolista10:.2f} segundos para fazer a busca numa lista de 10000 itens")

inicio_a = time.time()
print(buscaBinaria(lista100000,random.randint(1,1000000)))
fim_a= time.time()
tempolista10 = fim_a -inicio_a
print(f"Demorou {tempolista10:.2f} segundos para fazer a busca numa lista de 100000 itens")

