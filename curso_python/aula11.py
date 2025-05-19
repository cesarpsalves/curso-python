# Precedência de operadores

# Na programação temos a ordem de precedência dos operadores que são
# () parenteses
# ** potência
# * / // % multiplicação, divisão, divisão inteira, resto da divisão
# + - adição, subtração

conta_1 = 1 + 1 ** 5 + 5 
print(conta_1)

# No exemplo acima a ordem de precedência é a seguinte:
# 1 + 1 ** 5 + 5
# 1 + 1 + 5 
# 2 + 5
# 7

conta_2 = (1 + 1) ** (5 + 5)
print(conta_2)

# No exemplo acima a ordem de precedência é a seguinte:
# (1 + 1) ** (5 + 5)
# 2 ** 10
# 1024
