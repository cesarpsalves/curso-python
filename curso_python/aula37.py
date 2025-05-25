"""
Repetições
while (enquanto)
Executa uma ação enquanto uma condição for verdadeira
= += -= *= /= //= **= %=

Parte 4

while + continue
"""

contador = 0

while contador <= 50:
    contador += 1
    
    if contador == 10:
        print('Pule o 10')
        continue
        
    print(contador)
    if contador == 30:
        break