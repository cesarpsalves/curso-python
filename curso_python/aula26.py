"""
Formatação básica de string
s - string
d e i - int
f - float
.<numero de digitos>f - quantidade de casas decimais
x e X - Hexadecimal
(Carectere)(><^)(quantidade)
> - Esquerda
< - Direita
^ - Centro
= - Força o numero aparecer antes dos zeros
Sinal - + ou -
Ex.: 0>-100,.1f
Conversion flags - !r !s !a
"""

variavel = 'ABC'
print(f'{variavel}')
print(f'{variavel: >10}')
print(f'{variavel: <10}.')
print(f'{variavel: ^10}')
print(f'{1000.6565564546:0=+10,.1f}')
print(f'O hexadecimal de 1500 é {1500:08X}')