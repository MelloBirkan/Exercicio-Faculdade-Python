import random
import statistics


def espaco():
    print('-'*27)


def escrita():
    arquivo_base = open('/Users/MBirkan/Library/Mobile Documents/com~apple~CloudDocs/Faculdade/Segundo Semestre/Python/Lab_Algortimos_e_Programacao_II/Arquivos/Arquivo_aula3_Lab_Algoritmos_II_Exercicio3','w')
    zero = 0
    while zero < 10000:
        arquivo_base.write(str(random.randrange(0,10000))+'\n')
        zero += 1
    arquivo_base.close()

def leitura():
    leitura_arquivo = open('/Users/MBirkan/Library/Mobile Documents/com~apple~CloudDocs/Faculdade/Segundo Semestre/Python/Lab_Algortimos_e_Programacao_II/Arquivos/Arquivo_aula3_Lab_Algoritmos_II_Exercicio3','r')
    for x in leitura_arquivo:
        linha = int(leitura_arquivo.readline().rstrip('\n'))
        if linha < 1000:
            grupo_A.append(linha)
        if 1000 <= linha <2000:
            grupo_B.append(linha)
        if 2000 <= linha < 3000:
            grupo_C.append(linha)
        if 3000 <= linha < 4000:
            grupo_D.append(linha)
        if 4000 <= linha < 5000:
            grupo_E.append(linha)
        if 5000 <= linha < 6000:
            grupo_F.append(linha)
        if 6000 <= linha < 7000:
            grupo_G.append(linha)
        if 7000 <= linha < 8000:
            grupo_H.append(linha)
        if 8000 <= linha < 9000:
            grupo_I.append(linha)
        if 9000 <= linha < 10000:
            grupo_J.append(linha)
    leitura_arquivo.close()
grupo_A = []
grupo_B = []
grupo_C = []
grupo_D = []
grupo_E = []
grupo_F = []
grupo_G = []
grupo_H = []
grupo_I = []
grupo_J = []
escrita()
leitura()
reultado_mediana = (f'Mediana do Grupo A) {statistics.median(grupo_A)},\nMediana do Grupo B) {statistics.median(grupo_B)}'
f'\nMediana do Grupo C) {statistics.median(grupo_C)},\nMediana do Grupo D) {statistics.median(grupo_D)},'
f'\nMediana do Grupo E) {statistics.median(grupo_E)},\nMediana do Grupo F) {statistics.median(grupo_F)},'
f'\nMediana do Grupo G) {statistics.median(grupo_G)},\nMediana do Grupo H) {statistics.median(grupo_H)},'
f'\nMediana do Grupo I) {statistics.median(grupo_I)},\nMediana do Grupo J) {statistics.median(grupo_J)}')
print(reultado_mediana)
espaco()
resultado_media = (f'Media do Grupo A) {statistics.mean(grupo_A)},\nMedia do Grupo B) {statistics.mean(grupo_B)}'
f'\nMedia do Grupo C) {statistics.mean(grupo_C)},\nMedia do Grupo D) {statistics.mean(grupo_D)},'
f'\nMedia do Grupo E) {statistics.mean(grupo_E)},\nMedia do Grupo F) {statistics.mean(grupo_F)},'
f'\nMedia do Grupo G) {statistics.mean(grupo_G)},\nMedia do Grupo H) {statistics.mean(grupo_H)},'
f'\nMedia do Grupo I) {statistics.mean(grupo_I)},\nMedia do Grupo J) {statistics.mean(grupo_J)}')
print(resultado_media)
espaco()
resultado_moda = (f'Moda do Grupo A) {statistics.mode(grupo_A)},\nModa do Grupo B) {statistics.mode(grupo_B)}'
f'\nModa do Grupo C) {statistics.mode(grupo_C)},\nModa do Grupo D) {statistics.mode(grupo_D)},'
f'\nModa do Grupo E) {statistics.mode(grupo_E)},\nModa do Grupo F) {statistics.mode(grupo_F)},'
f'\nModa do Grupo G) {statistics.mode(grupo_G)},\nModa do Grupo H) {statistics.mode(grupo_H)},'
f'\nModa do Grupo I) {statistics.mode(grupo_I)},\nModa do Grupo J) {statistics.mode(grupo_J)}')
print(resultado_moda)


