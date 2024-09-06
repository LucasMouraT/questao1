import json

with open('dados.json', 'r') as file:
    faturamento = json.load(file)

faturamento_valido = [dia['valor'] for dia in faturamento if dia['valor'] > 0]

menor_valor = min(faturamento_valido)
maior_valor = max(faturamento_valido)

media_mensal = sum(faturamento_valido) / len(faturamento_valido)

dias_acima_da_media = len([valor for valor in faturamento_valido if valor > media_mensal])

print(f"Menor valor de faturamento: R$ {menor_valor:.2f}")
print(f"Maior valor de faturamento: R$ {maior_valor:.2f}")
print(f"Número de dias com faturamento acima da média mensal: {dias_acima_da_media}")