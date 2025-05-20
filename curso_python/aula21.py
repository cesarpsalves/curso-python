# Operadores Lógicos
# and(e), or(ou), not(não
# and - todas as condições precisam ser verdadeiras para retornar True
# or - pelo menos uma das condições precisa ser verdadeira para retornar True
# not - inverte o valor booleano

# Aula de and (E)

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'

if entrada == 'E' and senha_digitada == senha_permitida:
    print('Entrou...')
else:
    print('Saiu...')

    if 1 and 1:
        print(True and 1 and False)