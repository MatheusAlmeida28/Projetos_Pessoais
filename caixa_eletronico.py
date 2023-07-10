def calcular_notas(valor):
    notas_20 = valor // 20
    valor %= 20
    notas_10 = valor // 10
    valor %= 10
    notas_5 = valor // 5
    valor %= 5
    notas_2 = valor // 2
    
    notas_usadas = []
    if notas_20 > 0:
        notas_usadas.append(f"Notas de R$20: {notas_20}")
    if notas_10 > 0:
        notas_usadas.append(f"Notas de R$10: {notas_10}")
    if notas_5 > 0:
        notas_usadas.append(f"Notas de R$5: {notas_5}")
    if notas_2 > 0:
        notas_usadas.append(f"Notas de R$2: {notas_2}")
    
    return notas_usadas

# Solicitar valor para saque
valor_saque = int(input("Digite o valor que deseja sacar: "))

# Calcular as notas usadas
notas_usadas = calcular_notas(valor_saque)

# Exibir o resultado
print(f"Valor solicitado: R${valor_saque}")
for nota in notas_usadas:
    print(nota)
