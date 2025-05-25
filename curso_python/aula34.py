"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira

Parte 1
"""

condicao = True

while condicao:
    nome = input('Qual é o seu nome? ')
    print(f'Olá {nome}')

    if nome == 'sair':
        break