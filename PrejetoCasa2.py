from time import sleep
print('QUANTAS TOMADAS DEVEM TER EM UM CÔMODO?\n')
opção = 0
while opção !=4:
    print("""    [1]Cozinha
    [2]Sala
    [3]Quarto
    [4]Sair do programa\n\n""")
    opção = int(input('Escolha uma das opções: '))
    opção2 = 0
    while opção2 !=4:
        print("""        [1] 4 Metros
        [2] 6 Metros
        [3] 8 Metros
        [4] Sair do programa\n\n""")
        opção2 = int(input('Escolha a metragem: '))
        if opção == 1:
            if opção2 == 1:
                print('2 Tomadas')
        if opção == 1:
            if opção2 == 2:
                print('3 Tomadas')
        if opção == 1:
            if opção2 == 3:
                print('1 Tomada a cada 5 Metros')
        if opção == 2:
            if opção2 == 1:
                print('2 Tomadas')
        if opção == 2:
            if opção2 == 2:
                print('1 Tomada a cada 5 Metros')
        if opção == 2:
            if opção2 == 3:
                print('1 Tomada a cada 5 Metros')
        if opção == 3:
            if opção2 == 1:
                print('3 Tomadas')
        if opção == 3:
            if opção2 == 2:
                print('1 Tomada a cada 5 Metros')
        if opção == 3:
            if opção2 == 3:
                print('1 Tomada a cada 5 Metros')
        if opção == 4:
            print('Volte sempre!\n\n')
        if opção2 == 4:
            print('Volte sempre!\n\n')
        else:
            print('Espero ter ajudado!!')
        sleep(6)
#MayaraRk