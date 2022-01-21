import random
import time


def particao(lista, inicio, fim):
    pivo = inicio
    for i in range(inicio + 1, fim + 1):
        if lista[i] <= lista[inicio]:
            pivo += 1
            lista[i], lista[pivo] = lista[pivo], lista[i]
    lista[pivo], lista[inicio] = lista[inicio], lista[pivo]
    return pivo


def quicksort(lista, inicio=0, fim=None):
    if fim is None:
        fim = len(lista) - 1
    def _quicksort(lista, inicio, fim):
        if inicio >= fim:
            return
        pivo = particao(lista, inicio, fim)
        _quicksort(lista, inicio, pivo - 1)
        _quicksort(lista, pivo + 1, fim)
    return _quicksort(lista, inicio, fim)


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
quicksort(lista10)
fim_a= time.time()
tempolista = fim_a -inicio_a
print(lista10)
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 10 itens")

print(lista100)
inicio_a = time.time()
quicksort(lista100)
fim_a= time.time()
tempolista = fim_a -inicio_a
print(lista100)
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 100 itens")

print(lista1000)
inicio_a = time.time()
quicksort(lista1000)
fim_a= time.time()
tempolista = fim_a -inicio_a
print(lista1000)
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 1000 itens")

print(lista10000)
inicio_a = time.time()
quicksort(lista10000)
fim_a= time.time()
tempolista = fim_a -inicio_a
print(lista10000)
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 10000 itens")

#print(lista100000) Prof deixei comentado pois era uma lista muito grande.
inicio_a = time.time()
quicksort(lista100000)
fim_a= time.time()
tempolista = fim_a -inicio_a
#print(lista100000) Prof deixei comentado pois era uma lista muito grande.
print(f"Demorou {tempolista:.2f} segundos para fazer a ordenação numa lista de 100000 itens")

