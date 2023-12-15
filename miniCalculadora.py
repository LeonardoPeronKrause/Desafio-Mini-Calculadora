from time import sleep
primeiro = float(input('Digite um valor: '))
segundo = float(input('Digite outro valor: '))
opcao = 0

while opcao != 5:
    print('')
    print('[1] SOMAR \n[2] MULTIPLICAR \n[3] MAIOR VALOR \n[4] NOVOS NÚMEROS \n[5] SAIR DO PROGRAMA')
    print('')


    opcao = int(input('Qual a opção você deseja? '))
    if opcao == 1:
        resultado1 = primeiro + segundo
        print('A soma entre {:.2f} + {:.2f} é {:.2f}.'.format(primeiro,segundo,resultado1))
    elif opcao == 2:
        resultado2 = primeiro * segundo
        print('A multiplicação entre {:.2f} X {:.2f} é {:.2f}.'.format(primeiro,segundo,resultado2))
    elif opcao == 3:
        if primeiro > segundo:
            print('O número {} é maior que o número {}.'.format(primeiro,segundo))
        elif primeiro == segundo:
            print('Os números {} e {} são iguais.'.format(primeiro,segundo))
        else:
            print('O número {} é maior que o numero {}.'.format(segundo,primeiro))
    elif opcao == 4:
        print('Você escolheu digitar novos números: ')
        primeiro = float(input('Digite o novo valor para o primeiro número: '))
        segundo = float(input('Digite o novo valor para o segundo número: '))
    elif opcao == 5:
        print('Você pediu para sair do programa! Tchau tchau...')
        break
    else:
        print('Digite um valor válido!')
        
print('=-=' * 10)
sleep(1)
print('Fim do programa. Volte sempre!')
