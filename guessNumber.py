print('-------------------Guess the Number-------------------')
print('\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988')
print('Menu inicial')
print('\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988')
op = 1
jogo = False
tent = 0
vezes = 0
media = 0
while op != 0:
    print('1-Jogar')
    print('2-Regras')
    print('0-Sair')
    op = int(input('Selecione uma das opções acima: '))

    if op == 1:
        var = 0
        tent = 0
        soma = 0
        vezes = 0
        repeticao = True
        while repeticao:
            from random import *
            num = randrange(1, 1000)
            vezes = vezes + 1
            while var != num:
                var = int(input('Tente acertar o valor gerado entre 1 e 1000: '))
                if var > num:
                    print('\nO valor digitado é maior que o gerado.\n')
                elif var < num:
                    print('\nO valor digitado é menor que o gerado.\n')
                else:
                    print('\nEste é o valor\n')
                if tent > 5:
                    if num % 2 == 0:
                        print('O número gerado é par.\n')
                    else:
                        print('O número gerado é impar.\n')
                tent = tent + 1

            print(f'\n\nVocê acertou, o valor gerado foi {num}')
            print(f'Número de tentativas: {tent}\n')
            if tent <= 5:
                print('\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988')
                print('Flawless Victory!')
                print('\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988')
            else:
                print('\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988''\U0001F988')
            soma = soma + tent
            media = soma / vezes
            selecao = int(input('\nDigite 0 se quiser encerrar as tentativas: '))
            if selecao == 0:
                repeticao = False
                print(f'Sua média de tentativas até o acerto foi de: {media}\n\n')
            else:
                repeticao = True
                tent = 0
                var = 0

    elif op == 2:
        print('\n\nSerá gerado um número aleatório entre 1 e 1000.')
        print('Você tenta acertar o número com tentativas ilimitadas.')
        print('Ao sair, você recebe uma média de suas tentativas até o acerto.\n\n')
    elif op != 0:
        print('Opção inválida.\n\n')
    else:
        print('\n\nVocê encerrou suas operações.')
