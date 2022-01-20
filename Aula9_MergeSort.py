import random
import time


def merge(lista, aux, esquerda, meio, direita):
    for k in range(esquerda, direita + 1):
        aux[k] = lista[k]
    i = esquerda
    j = meio + 1
    for k in range(esquerda, direita + 1):
        if i > meio:
            lista[k] = aux[j]
            j += 1
        elif j > direita:
            lista[k] = aux[i]
            i += 1
        elif aux[j] < aux[i]:
            lista[k] = aux[j]
            j += 1
        else:
            lista[k] = aux[i]
            i += 1


def mergesort(lista, aux, esquerda, direita):
    if direita <= esquerda:
        return
    meio = (esquerda + direita) // 2
    mergesort(lista, aux, esquerda, meio)
    mergesort(lista, aux, meio + 1, direita)
    merge(lista, aux, esquerda, meio, direita)


lista10 = []
for x in range(10):
    lista10.append(random.randint(1, 10))
aux10 = [0] * len(lista10)

lista100 = []
for x in range(100):
    lista100.append(random.randint(1, 100))
aux100 = [0] * len(lista100)

lista1000 = []
for x in range(1000):
    lista1000.append(random.randint(1, 1000))
aux1000 = [0] * len(lista1000)

lista10000 = []
for x in range(10000):
    lista10000.append(random.randint(1, 10000))
aux10000 = [0] * len(lista10000)

lista100000 = []
for x in range(100000):
    lista100000.append(random.randint(1, 1000000))
aux100000 = [0] * len(lista100000)

print(lista10)
inicio_a = time.time()
mergesort(lista10, aux10, 0, len(lista10) - 1)
fim_a= time.time()
tempolista = fim_a -inicio_a
print(lista10)
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 10 itens")

print(lista100)
inicio_a = time.time()
mergesort(lista100, aux100, 0, len(lista100) - 1)
fim_a= time.time()
tempolista = fim_a -inicio_a
print(lista100)
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 100 itens")

print(lista1000)
inicio_a = time.time()
mergesort(lista1000, aux1000, 0, len(lista1000) - 1)
fim_a= time.time()
tempolista = fim_a -inicio_a
print(lista1000)
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 1000 itens")

print(lista10000)
inicio_a = time.time()
mergesort(lista10000, aux10000, 0, len(lista10000) - 1)
fim_a= time.time()
tempolista = fim_a -inicio_a
print(lista10000)
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 10000 itens")

#print(lista100000) Prof deixei comentado pois era uma lista muito grande.
inicio_a = time.time()
mergesort(lista100000, aux100000, 0, len(lista100000) - 1)
fim_a= time.time()
tempolista = fim_a -inicio_a
#print(lista100000) Prof deixei comentado pois era uma lista muito grande.
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 100000 itens")