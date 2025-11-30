qtd_casas,qtd_caminhaos = map(int,input().split(" "))

casas_abastecidas = list()

for i in range(0,qtd_casas):
    casas_abastecidas.append(0)

for caminhao in range(0,qtd_caminhaos):
    de,ate,litros = map(int,input().split(" "))
    
    for i in range(de,ate + 1):
        casas_abastecidas[i] += litros


for casa in casas_abastecidas:
    print(casa,end=" ")
