# Exercício de concatenação
# Crie um programa que:
# 1. Peça ao usuário:
# - o nome
# - a idade
# - a cidade

# 2. Depois mostre a seguinte frase usando concatenação ou f-string:

# "Olá, meu nome é João, tenho 25 anos e moro em Fortaleza."

# Os valores devem ser substituídos pelos dados digitados pelo usuário.

name = "João"
age = 25
city = "Fortaleza"

print(f"Olá, meu nome é {name}, eu tenho {age} e moro em {city}.")
print("Olá, meu nome é " + name + ", eu tenho " + str(age) +" e moro em " + city + ".")