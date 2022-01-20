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
lista_numerica_auxiliar = []  # Lista ultilizada para conseguir somar usando a função criada 'soma'.


def soma(lista):
    # Função ultilizada para somar somar os numeros de uma lista, uma alternativa ao sum().
    soma_total = 0
    for n in lista:
        soma_total += n
    return soma_total


def multipl_russa(a, b):
    if a == 1:
        lista_numerica_auxiliar.append(b)
        return soma(lista_numerica_auxiliar)
    elif a % 2 != 0:  # Verificar se o 'a' é primo.
        lista_numerica_auxiliar.append(b)  # Numero 'b' adicionado a uma lista que irá somar todos os resultados.
        return multipl_russa(a // 2, b * 2)
    else:  # Se o numero não for primo, não adicionamos ele na lista, e fazemos a recursividade após isso.
        return multipl_russa(a // 2, b * 2)


print(f"O resultado da multiplicação de 27 por 82 é: {multipl_russa(27, 82)}")

lista_numerica_auxiliar = []#zerado para poder usar o 'input'
num_1 = int(input("Escolha um numero para multiplcar: "))
num_2 = int(input("Escolha outro numero para multiplcar: "))
print(f"O resultado da multiplicação de {num_1} por {num_2} é: {multipl_russa(num_1, num_2)}")
