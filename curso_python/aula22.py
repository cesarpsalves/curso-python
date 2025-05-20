# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None que é usado pra representar um não valor

# Aula de or (OU)

entrada = input('[E]ntrar [S]air: ')
senha_digitada = input('Senha: ')

senha_permitida = '1234'

if (entrada == 'E' or entrada == 'e') and senha_digitada == senha_permitida:
    print('Entrou...')
else:
    print('Saiu...')