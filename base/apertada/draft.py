lista = list()

for i in range(0,5):
    valor = int(input())
    lista.append(valor)
    if i == 0:
        menor = valor
    else:
        if menor > valor:
            menor = valor    
print(menor)
# OU
# print(min(lista)) <-- isso elimina todos as condições