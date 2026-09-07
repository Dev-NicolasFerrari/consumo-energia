# Calculadora de consumo elétrico inteligente
# Autor: Nicolas Ferrari

# Entrada
nome_aparelho = input("Digite o tipo de aparelho: ")
voltagem_watt = float(input("Digite a voltagem do aparelho em watts(W): "))
tempo_uso = float(input("Digite o tempo médio de uso diário em horas: "))

# Processamento
consumo_mensal = (voltagem_watt * tempo_uso * 30) / 1000
valor_fatura = consumo_mensal * 0.75

# Saída
print(f"\nAparelho: {nome_aparelho}")
print(f"\nEstimativa de consumo mensal: {consumo_mensal:.2f}")
print(f"\nValor estimado da fatura: R${valor_fatura:.2f}")