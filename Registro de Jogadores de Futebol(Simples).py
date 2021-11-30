gols = []
jogador = {}
jogadores = []
print('-----------REGISTRO DE JOGADORES-------------')
while True:
    jogador.clear()
    gols.clear()
    jogador['nome'] = str(input('Nome do Jogador: ')).title()
    partida = int(input('Quantas partidas jogou?: '))
    for gol in range(0, partida):
        gols.append(int(input(f'Quantos gol(s) o {jogador["nome"]} fez na partida {gol+1}?: ')))
    jogador['gols'] = gols[:]
    jogador['total'] = sum(gols)
    jogadores.append(jogador.copy())
    while True:
        continuar = str(input('Quer continuar?[S/N]: ')).upper()[0]
        if continuar in 'SN':
            break
        print('Erro.Digite o valor certo')
    if continuar == 'N':
        break
print('-='*25)
print('COD       JOGADOR       GOLS         TOTAL')
for key, value in enumerate(jogadores):
    print(f'{key:>3}', end='')
    for k in value.values():
        print(f'{str(k):>13}', end='')
    print()
print('-='*25)
while True:
    resposta = int(input('Mostrar dados de qual jogador: '))
    for key, value in enumerate(jogadores):
        if resposta == key:
            print(f'levantamento do jogador {value["nome"]}')
            print('-='*25)
            for p in range(len(value['gols'])):
                print(f'No jogo {p+1},{value["nome"]} fez {value["gols"][p]} gols')
            print('-='*30)
    if resposta == 999:
        break
print('Fim do Programa')
