# Exercício: Operadores de atribuição

# 1. Crie uma variável chamada saldo e dê a ela o valor 1000.

# 2. Faça as seguintes operações usando operadores de atribuição:

# - Adicione 200 ao saldo
# - Subtraia 150 do saldo
# - Multiplique o saldo por 2
# - Divida o saldo por 5

# 3. Depois de cada operação, mostre o valor do saldo na tela.

# Exemplo de saída esperada:

# Saldo inicial: 1000
# Depois de adicionar 200: 1200
# Depois de subtrair 150: 1050
# Depois de multiplicar por 2: 2100
# Depois de dividir por 5: 420

saldo = 1000
print(f"Saldo inicial: {saldo}")

saldo += 200
print(f"Depois de adicionar 200: {saldo}")

saldo -= 150
print(f"Depois de subtrair 150: {saldo}")

saldo *= 2
print(f"Depois de multiplicar por 2: {saldo}")

saldo //= 5
print(f"Depois de dividir por 5: {saldo}")