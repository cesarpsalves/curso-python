primeiro_valor = input("Digite um valor: ")
segundo_valor = input("Digite outro valor: ")

primeiro = primeiro_valor
segundo = segundo_valor

if primeiro > segundo:
    print(f'O primeiro valor {primeiro} é maior que o segundo valor {segundo}')
elif primeiro < segundo:
    print(f'O segundo valor {segundo} é maior que o primeiro valor {primeiro}')
else:
    print(f'O primeiro valor {primeiro} é igual o segundo valor {segundo}')
    
