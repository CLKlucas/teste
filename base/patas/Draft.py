chute_bento = int(input())
chute_cebola = int(input())
qtd_animais = int(input())
soma = 0
lista = list()

for i in range(0,qtd_animais):
    animal = str(input())
    if animal == "v" or animal == "c":
        soma += 4
    elif animal == "g":
        soma += 2 


lista.append(abs(soma - chute_bento))
lista.append(abs(soma - chute_cebola))

if lista[0] == lista[1]:
    print(soma)
    print("empate")
else:
    if lista[0] == min(lista):
        print(soma)
        print("Chico Bento")
    else:
        print(soma)
        print("Cebolinha")    