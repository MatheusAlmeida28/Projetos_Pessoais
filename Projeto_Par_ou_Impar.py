from time import sleep


print('-'*30)
print('Vamos descobrir se um valor é Par ou ímpar')
print('-'*30)

while True:
    try:
        valor = int(input('Digite uma valor inteiro: '))
        if valor % 2 == 0:
            sleep(1)
            print('-'*30)
            print(f'O valor: {valor} é um número Par')      
        else:
            sleep(1)
            print('-'*30)
            print(f'O valor é: {valor} é um número Ímpar')
    except:
        print('-'*30)
        print('Digite um valor válido')
        continue 
    try:
        print('-'*30)
        continuar = str(input('Quer continuar?: ')).lower()
        if continuar in 's':
            continue
        if continuar not in 'sn':
            print('Digite uma valor válido')
            print('-'*30)
            continuar = str(input('Quer continuar?: ')).lower()
            if continuar == 'n':
                break
            else:
                continue
        if continuar == 'n':
            break
    except:
        print('Digite um valor válido')
    break
print('Fim do código')

