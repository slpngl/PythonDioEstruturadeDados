valor_inicial = float(input())
taxa_juros = float(input())
periodo = int(input())

valor_final = valor_inicial * (1+taxa_juros)**periodo

print("Valor final do investimento: R$ %.2f" %valor_final)

