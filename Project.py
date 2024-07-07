from time import sleep

while True:
    cell = input('Pra começar, qual sua Preferência, \033[33mAndroid\033[m ou \033[34miPhone\033[m? ').upper()

    if cell == 'IPHONE':
        while True:
            print('Atualmente temos, o iPhone \033[34m10, 12 e 15,\033[m todos nas \033[1mversões padrões\033[m')
            a = input('Escolha a Versão: ').upper()

            sleep(2)

            if a == '10' or a == 'X':
                print('Esse tá \033[34mR$1.000\033[m')
                break
            elif a == '12':
                print('Esse tá \033[34mR$1.500\033[m')
                break
            elif a == '15':
                print('Esse tá \033[34mR$5.000\033[m')
                break
            else:
                print('Este está em falta')
        break
    else:
        print('Por favor, escolha entre \033[33mAndroid\033[m ou \033[34miPhone\033[m:')

    if cell == 'ANDROID':
        while True:
            print('Atualmente em \033[33mAndroid\033[m, temos \033[31mSansung\033[m e \033[35mMotorola\033[m')
            b = input('Sansung ou Motorola? ').upper()
            sleep(2)
            if b == 'SANSUNG':
                print('Temos o \033[37mA10, A15, S20 e S24\033[m. Todos em suas Versões Padrões.')
                sa = input('Qual será o Escolhido? ').upper()
                sleep(2)
                if sa == 'A10':
                    print('Esse tá \033[31mR$800,00\033[m')
                    break

                elif sa == 'A15':
                    print('Esse tá \033[31mR$1.200\033[m')
                    break

                elif sa == 'S20':
                    print('Esse tá \033[31mR$2.000\033[m')
                    break

                elif sa == 'S24':
                    print('Esse tá \033[31mR$3.100\033[m')
                    break

                else:
                    print('Este está em Falta!')

            if b == 'MOTOROLA':
                print('Temos o \033[37mg22\033[m e \033[37mg42\033[m')
                mo = input('Qual será o Escolhido? ').upper()
                sleep(2)
                if mo == 'G22':
                    print('Esse tá \033[35mR$1.000\033[m')
                    break

            elif mo == 'G42':
                print('Esse tá \033[35mR$1.600\033[m')
                break

            else:
                print('Esse tá em Falta!')
