import json

# Lê o arquivo JSON
with open('C:\\src\\python\\target_teste\\dados.json', 'r') as f:
    dados = json.load(f)

# Inicializa as variáveis de mínimo e máximo
minimo_valor = float('inf')
maximo_valor = float('-inf')
minimo_dia = str
maximo_dia = str

# Calcula a média mensal, ignorando dias sem faturamento
soma = 0
dias_com_faturamento = 0
for dia in dados:
    valor = dia['valor']
    dia_limpo = dia['dia']
    if valor > maximo_valor:
        maximo_valor = valor
        maximo_dia = dia_limpo
    if valor < minimo_valor:
        minimo_valor = valor
        minimo_dia = dia_limpo
    if valor > 0:
        soma += valor
        dias_com_faturamento += 1
media = soma / dias_com_faturamento

# Conta o número de dias com faturamento acima da média
dias_acima_da_media = 0
for dia in dados:
    valor = dia['valor']
    if valor > media:
        dias_acima_da_media += 1

# Imprime as informações calculadas
print(f"O menor valor de faturamento foi R$ {minimo_valor:.2f}, registrado no dia {minimo_dia}")
print(f"O maior valor de faturamento foi R$ {maximo_valor:.2f}, registrado no dia {maximo_dia}")
print(f"{dias_acima_da_media} dias tiveram faturamento acima da média mensal, no valor de R$ {media:.2f}")
