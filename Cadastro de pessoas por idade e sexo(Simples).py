galera = []
pessoa = {}
soma = media = 0
while True:
    pessoa.clear()
    pessoa['Nome'] = str(input('Nome: ')).title()
    while True:
        pessoa['Sexo'] = str(input('Sexo: [M/F]')).upper()[0]
        if pessoa['Sexo'] in 'MF':
            break
        print('ERRO! Por Favor, digite apenas M ou F.')
    pessoa['idade'] = int(input('Idade: '))
    soma += pessoa['idade']
    galera.append(pessoa.copy())
    while True:
        resp = str(input('Quer continuar? [S/N]: ')).strip().upper()
        if resp in 'SN':
            break
        print('Erro! Responda apenas S ou N.')
    if resp == 'N':
        break
print('-='*30)
print(f'Ao todo temos {len(galera)} pessoas cadastradas')
media = soma / len(galera)
print(f'A média das idades são {media:5.2f}')
print('As Mulheres cadastradas foram: ', end='')
for p in galera:
    if p['Sexo'] == 'F':
        print(f'{p["Nome"]} ', end='')
print()
print('lista de idade acima da média: ', end='')
for p in galera:
    if p['idade'] >= media:
        print(f'{p["Nome"]} ', end='')
print()
