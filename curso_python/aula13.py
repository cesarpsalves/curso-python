# Descobrindo IMC

nome = 'Luciana'
peso = 65
altura = 1.73

# O IMC é calculado pela fórmula peso / (altura ** 2)
# O IMC ideal varia de 18.5 a 24.9
imc = peso / (altura ** 2)
print(nome, 'tem', altura, 'de altura e pesa', peso, 'kg.')
print('O IMC de', nome, 'é', imc)

# Aula de formatação de strings
print(f'{nome} tem {altura} de altura e pesa {peso} kg.')
print(f'O IMC de {nome} é {imc:.2f}')

# O f na frente da string é chamada de f-string
# O .2f é um método que limita o número de casas decimais
# O :.2f é chamado de f-string formatada    