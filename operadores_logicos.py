# Exercício: Operadores lógicos

# 1. Crie duas variáveis:
# idade = 20
# tem_carteira = True

# 2. Mostre na tela o resultado das seguintes verificações:

# - A pessoa pode dirigir? 
# - A pessoa é menor de idade? 
# - A pessoa NÃO tem carteira? 

# Exemplo de saída esperada:

# Pode dirigir: True
# É menor de idade ou não tem carteira: False
# Não tem carteira: False


idade = 20
tem_carteira = True

print(f"Pode dirigir: {idade >= 18 and tem_carteira}")
print(f"É menor de idade ou não tem carteira: {idade < 18 or not tem_carteira}")
print(f"Não tem carteira: {not tem_carteira}")

