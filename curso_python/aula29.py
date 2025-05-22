"""
Introdução ao try/except
try -> tentar execurae o código
except -> ocorreu algum erro ao tentar executar
"""

numero_str = input('Digite um número: ')

try:
    numero_int = int(numero_str)
    print(f'O dobro de {numero_str} é {numero_int * 2}')
except:
    print('Isso não é um número.')