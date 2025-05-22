"""
Flag (Bandeira) - Marcar um local
None = Não valor
is e is not = é ou não é (tipo, valor, identidade)
id = identidade
"""

v1 = 'a'
v2 = 'b'

print(id(v1))
print(id(v2))

# O comando id fala a identidade e caso exista um mesmo valor por exemplo numa variavél
# o python pra não gastar memoria usa o mesmo id

condicao = True
passou_no_if = None

if condicao:
    print('Faça algo')
    passou_no_if = True
else:
    print('Não faça algo')

if passou_no_if is None:
    print('Não passou no if')

if passou_no_if is not None:
    print('Passou no if')