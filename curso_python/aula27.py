"""
Fatiamento de strings
012345678  indice positivo
Olá mundo
-987654321 indice negativo
Fatiamento [1:f:p] [::]
Obs.: a função len retorna a qtd
de carecteres da str
"""

variavel = 'Olá mundo'
print(variavel[2:6])       # Escolhe o indice inicial e final
print(len(variavel))       # Conta quantidade de carecteres
print(variavel[0:9:2])     # Além de escolher o indice dar pra contar passos que vamos pular [1:f:p]
print(variavel[8:]) # Invertido