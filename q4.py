# Valores de faturamento mensal por estado
faturamento_mes = {
    'São Paulo': 67836.43,
    'Rio de Janeiro': 36678.66,
    'Minas Gerais': 29229.88,
    'Espirito Santo': 27165.48,
    'Outros': 19849.53
}

# Cálculo do valor total mensal da distribuidora
valor_total_mes = sum(faturamento_mes.values())

# Cálculo do percentual de representação de cada estado
for estado, valor in faturamento_mes.items():
    percentual = (valor / valor_total_mes) * 100
    print(f'{estado}: {percentual:.2f}%')
