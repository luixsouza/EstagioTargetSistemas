import json

# Supondo que os dados estejam neste formato no arquivo faturamento.json
# {
#   "faturamento": [100, 200, 300, 0, 400, ...]
# }

def calcular_faturamento():
    with open('/home/luis/Área de Trabalho/EstágioTarget/Faturamento.json', 'r') as file: #Alterar a critério
        dados = json.load(file)

    faturamento = dados['faturamento']
    faturamento_validos = [valor for valor in faturamento if valor > 0]

    menor_valor = min(faturamento_validos)
    maior_valor = max(faturamento_validos)
    media_mensal = sum(faturamento_validos) / len(faturamento_validos)

    dias_acima_media = sum(1 for valor in faturamento_validos if valor > media_mensal)

    return menor_valor, maior_valor, dias_acima_media

menor, maior, dias_acima_media = calcular_faturamento()
print(f"Menor valor: {menor}")
print(f"Maior valor: {maior}")
print(f"Dias acima da média mensal: {dias_acima_media}")
