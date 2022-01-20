class Pessoa:
    def __init__(self, nome, indice, quantidade):
        self.nome = nome
        self.indice = indice
        self.quantidade = quantidade
ler_grupo1 = open(r"C:\Users\Pichau\iCloudDrive\Faculdade\Segundo Semestre\Python\Lab_Algortimos_e_Programacao_II\Exercicio entregas\Aula5_exercicio\Arquivos de apoio\grupo1.txt","r")
grupo1 = []
for linha in ler_grupo1:
    linha = ler_grupo1.readline().replace(";", "").replace(",", ".").rstrip("\n").split("\t")
    grupo1.append(linha)
pessoa1 = grupo1[1]
pessoa1=
pessoas = []
"""pessoas.append(Pessoa('Paulo Henrique', 0.9787, 32))
pessoas.append(Pessoa('Mayara', 0.3687, 97))
pessoas.append(Pessoa('Caio', 0.340, 46))"""

#print(pessoa.nome, pessoa.indice, pessoa.quantidade)



