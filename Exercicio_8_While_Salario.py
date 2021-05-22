quant_Empregados = int(input('Digite a quantidade de empregados: '))
contador_empregado = 0
contador_fem = somatorio_sal_masc = contador_masc = contador_resp_b = 0
while quant_Empregados != 0:
    contador_empregado += 1
    nome = input(f'Digite aqui o nome do empregado {contador_empregado}: ')
    sexo = input(f'Digite aqui o genero do empregado {contador_empregado} (F/M): ').upper()
    while sexo not in ('F','M'):
        sexo = input(f'Genero não reconhecido.Digite aqui o genero do empregado {contador_empregado}(F/M): ').upper()
    salario = float(input(f'Digite aqui o sálario do empregado {contador_empregado}: '))
    while salario <= 850.00:
        salario = float(input(f'Salário inferior que o minimo esperado (R$ 850,00). Digite aqui o sálario do empregado {contador_empregado}: '))
    if salario < 2000:
        salario_novo = salario * 1.085
    elif 2000 <= salario < 3000:
        salario_novo = salario * 1.065
        contador_resp_b +=1
    else:
        salario_novo = salario * 1.045
    print(f'--------------\nA) Salário reajustado do empregado {contador_empregado}: {salario_novo:.2f}\n----------------------')
    if sexo == 'M':
        contador_masc += 1
        somatorio_sal_masc += salario_novo
    if sexo == 'F':
        contador_fem += 1
    quant_Empregados -= 1
perc_fem = (contador_fem * 100) / contador_empregado
media = somatorio_sal_masc / contador_masc
print(f'-----------------------------------------\nB) {contador_resp_b} empregados tiveram um reajuste de 6.5%.')
print(f'C) R$ {media:.2f} foi a média do salário reajustado dos homens.')
print(f'D) {perc_fem:.1f}% é o percentual de empregados do genero feminino dentro do total de empregados.')