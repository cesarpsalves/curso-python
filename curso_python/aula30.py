"""
Boas práticas
CONSTANTE = "Variaveis" que não vão mudar
Muitas condições no mesmo if (ruim)
    <- Contagem de complexidade (ruim)
"""

# Dados do carro
velocidade = 30           # Velocidade atual do carro (km/h)
local_carro = 100         # Localização atual do carro na estrada (em km ou metros)

# Configuração do radar
RADAR_1 = 60             # Velocidade máxima permitida no radar 1
LOCAL_1 = 100            # Localização do radar 1
RADAR_RANGE = 1          # Alcance de atuação do radar (antes e depois do ponto)

# Verificações
velocidade_acima = velocidade > RADAR_1
dentro_do_radar = LOCAL_1 - RADAR_RANGE <= local_carro <= LOCAL_1 + RADAR_RANGE

# Resultado
if velocidade_acima and dentro_do_radar:
    print('Multado: acima da velocidade e dentro da área do radar.')
elif not velocidade_acima and dentro_do_radar:
    print('Passando pelo radar dentro da velocidade permitida.')
else:
    print('Fora da área do radar.')
