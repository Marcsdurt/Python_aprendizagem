# Exercício: Entrada e saída de dados

# 1. Peça ao usuário para digitar:
# - seu nome
# - sua idade

# 2. Depois mostre a seguinte frase:

# "Olá, João! Você tem 25 anos."

# Os valores devem ser os que o usuário digitou.

# Desafio extra:
# Mostre também o tipo da variável idade usando a função type().


name = input("Digite seu nome: ")
age = input("Digite sua idade: ")

print(f"Olá, {name}! Você tem {age} anos.")

print(type(age))

