salas = [10, 2, 1, 3, 0]
salas_disponiveis = [1, 2, 3, 4, 5]


def menu_cinema():
    menu = int(input('---------------------------\nOlá Bem-vindo ao cinema\n---------------------------\n(1)Ver salas disponíveis \n(2)Comprar ingressos\n(3) Sair\nSelecione entre 1, 2 ou 3: '))
    while menu not in (1,2,3):
        menu = int(input('Selecione entre 1, 2 ou 3: '))
    if menu == 1:
        for x in range(5):
            print(f'Sala {salas_disponiveis[x]}, tem {salas[x]} Lugares disponiveis.')
        voltar_Menu = input(f'Deseja voltar ao menu?(Digite "sim" para voltar) ').lower()
        while voltar_Menu != ('sim'):
            voltar_Menu = input(f'Opção invalida. Deseja voltar ao menu?(Digite "sim" para voltar) ').lower()
        if voltar_Menu == 'sim':
            menu_cinema()
        print('-'*27)
        menu_cinema()
    if menu == 3:
        print('Voce saiu do menu')
    else:
        qualsala = int(input(f'As salas disponiveis são: {salas_disponiveis}\nDeseja selecionar Qual sala? '))
        qualsala_menos_um = qualsala - 1
        if salas[qualsala_menos_um] == 0:
            print('Está sala lotada. Retornando ao menu!')
            print('-'*27)
            menu_cinema()
        imprimir_lugares = int(input(f'A sala {qualsala} possui {salas[qualsala_menos_um]} lugares disponiveis.\nQuantos lugares serão ocupados ? '))
        while imprimir_lugares > salas[qualsala_menos_um]:
            imprimir_lugares = int(input(f'Compra negada. A sala: {qualsala}, não possui todos esses lugares disponiveis, esta sala têm apenas {salas[qualsala_menos_um]} lugares disponiveis.\nDigite novamente quantos lugares serão ocupados  '))
        sala_atulizado = salas[qualsala_menos_um] - imprimir_lugares
        salas[qualsala_menos_um] = sala_atulizado
        voltar_Menu = input(f'Compra confirmada\nDeseja voltar ao menu?("sim/não") ').lower()
        while voltar_Menu not in('sim','nao','não'):
            voltar_Menu = input(f'Opção invalida. Deseja voltar ao menu?("sim/não") ').lower()
        if voltar_Menu == 'sim':
            menu_cinema()
        else:
            print('Compra finalizada!')


menu_cinema()
print('Volte sempre!')




