def imprime_vetor(vetor): 
    valores_int = list()

    for i in range(len(valores)):
        if vetor[i] != " ":
            valores_int.append(int(vetor[i]))

    print(valores_int)

cont = 0
qtd = int(input())
while cont != 1:
    valores = str(input()).split()
    if len(valores) == qtd:
        cont += 1
        imprime_vetor(valores)
    else:
        print(f"Tente novamente, coloque {qtd} elementos")
