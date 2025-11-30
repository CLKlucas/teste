cont = 0
lista = []
for i in range(3):
    numero = int(input())
    lista.append(numero)


for l in range(3):
    
    for i in range(len(lista)):
        
        if l != i:

            if(lista[l] == lista[i]):
                if cont < 3:
                    cont += 1
print(cont)