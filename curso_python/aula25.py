"""
Interpolação básica de strings
s - string
d e i - int
f - float
x e X - Hexadecimal
"""

nome = 'Paulo'
preco = 1000.95897643
variavel = '%s, o preço é R$ %.2f' % (nome, preco)
print(variavel)
print('O hexadecimal de %d é %04x' % (65500, 65500))
