# São considerados falsy
# 0 0.0 '' False
# Também existe o tipo None que é usado pra representar um não valor

# Aula de not (NÃO)

entrada = input('Senha: ')

senha_permitida = '1234'

if not entrada == senha_permitida:
    print('Saiu...')