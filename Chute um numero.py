from random import randint
pc = randint(1, 100)
cont = 0
while True:
    try:
        jogador = int(input('Digite um valor inteiro: '))
        if pc < jogador:
            print('Coloque um valor menor')
            cont += 1
        elif pc > jogador:
            print('Coloque um valor maior')
            cont += 1
        elif jogador == pc:
            break
    except:
        print('-'*30)
        print('Digite um valor válido')
        print('-'*30)
        continue
print('-'*30)
print(f'Você conseguiu! O número que você escolheu foi {jogador} e o meu foi {pc}')
print(f'E você conquistou isso com {cont} tentativas!')
print('-'*30)
