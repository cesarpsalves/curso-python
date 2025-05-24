"""
Faça um programa que peça ao usuário para digitar um número inteiro,
informe se este númer é par ou ímpar. Caso o usuário não digite um número
inteiro, informe que não é um número inteiro.
"""
inteiro = input('Digite um numero inteiro: ')

try:
    inteiro = int(inteiro)
    if inteiro % 2 == 0:
        print('Par')
    else:
        print('Impar')
except:
    print('Isso não é um número inteiro')


"""
Faça um programa que pergunte a hora ao usuário e, baseando-se no horário 
descrito, exiba a saudação apropriada. Ex. 
Bom dia 0-11, Boa tarde 12-17 e Boa noite 18-23.
"""

hora = input('Que horas são no formato 24: ')

try:
    hora = int(hora)
    if (hora >= 0) and (hora < 12):
        print('Bom dia!')
    elif (hora >= 12) and (hora < 18):
        print('Boa tarde!')
    elif (hora >= 18) and (hora < 23):
        print('Boa noite!')
    else:
        print('Digite um numero de 0 a 23.')
except:
    print('Isso não está no formato de horas')



"""
Faça um programa que peça o primeiro nome do usuário. Se o nome tiver 4 letras ou 
menos escreva "Seu nome é curto"; se tiver entre 5 e 6 letras, escreva 
"Seu nome é normal"; maior que 6 escreva "Seu nome é muito grande". 
"""

usuario = input('Digite um nome de usuario: ')



try:
    contarletras = len(usuario)
    if contarletras <= 4:
        print('Seu nome é curto!')
    elif (contarletras >= 5) and (contarletras < 7):
        print('Seu nome é normal!')
    elif contarletras > 6:
        print('Seu nome é muito grande!')
    else:
        print('Digite um nome')
except:
    print('Isso não está no formato de horas')
