lista_auxiliar = []
lista_auxiliar5 = []
lista_auxiliar7 = []




def dec2bin(n):
    if n == 0:
        hiindex = len(lista_auxiliar)-1
        for x in range(len(lista_auxiliar)//2):
            lista_auxiliar[x], lista_auxiliar[hiindex] = lista_auxiliar[hiindex], lista_auxiliar[x]
            hiindex-= 1
        transformar_str = [str(x) for x in lista_auxiliar]
        resultado = (''.join(transformar_str))
        return 1 and print(resultado)
    else:

        lista_auxiliar.append(n % 2)
        return dec2bin(n//2)



def dec2base5(n):
    if n == 0:
        hiindex = len(lista_auxiliar5)-1
        for x in range(len(lista_auxiliar5)//2):
            lista_auxiliar5[x], lista_auxiliar5[hiindex] = lista_auxiliar5[hiindex], lista_auxiliar5[x]
            hiindex-= 1
        transformar_str = [str(x) for x in lista_auxiliar5]
        resultado = (''.join(transformar_str))
        return 1 and print(resultado)
    else:
        lista_auxiliar5.append(n % 5)
        return dec2base5(n//5)


def dec2base7(n):
    if n == 0:
        hiindex = len(lista_auxiliar7)-1
        for x in range(len(lista_auxiliar7)//2):
            lista_auxiliar7[x], lista_auxiliar7[hiindex] = lista_auxiliar7[hiindex], lista_auxiliar7[x]
            hiindex-= 1
        transformar_str = [str(x) for x in lista_auxiliar7]
        resultado = (''.join(transformar_str))
        return 1 and print(resultado)
    else:
        lista_auxiliar7.append(n % 7)
        return dec2base7(n//7)


dec2bin(100)
dec2base5(100)
dec2base7(100)
