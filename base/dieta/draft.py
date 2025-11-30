dias = int(input())
soma = 0
for i in range(0,dias):
    calorias = int(input())
    soma += calorias

calorias_por_d = float(soma / dias)
print("%.1f" % (calorias_por_d))