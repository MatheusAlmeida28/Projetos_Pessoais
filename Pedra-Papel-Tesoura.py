from random import choice

computador = ['pedra','papel','tesoura']
pc = choice(computador)

print('Seja bem vindo ao Tic Tac Toe(Ver:0.1)')
print('-'*30)


while True:
    player = input('Digite a escolha: [1]-Pedra [2]-Papel [3]-Tesoura:')
    if player in '123':
        break
    else:
        print('Algo saiu errado ai')
        continue
if player == '1':
    player = 'pedra'
elif player == '2':
    player = 'papel'
elif player == '3':
    player = 'tesoura'

print('-'*30)
print(f'O jogador jogou {player} e o oponente jogou {pc}')
print('-'*30)

if pc == 'papel' and player == 'tesoura':
    x = print('Jogador ganhou!!!')
elif pc == 'tesoura' and player == 'papel':
    x= print('O Oponente venceu!!!')
elif pc == 'tesoura' and player == 'tesoura':
    x= print('Empate!!!')
elif pc == 'papel' and player == 'papel':
    x= print('Empate!!!') 
elif pc == 'pedra' and player == 'pedra':
    x= print('Empate!!!') 
elif pc == 'pedra' and player == 'papel':
    x = print('Jogador venceu!!!')
elif pc == 'papel' and player == 'pedra':
    x = print('O Oponente venceu!!!')
elif pc == 'tesoura' and player == 'pedra':
    x = print('Jogador venceu!!!')
elif pc == 'pedra' and player == 'tesoura':
    x = print('O Oponente venceu!!!')

