cont = 0
qtd = int(input())
if qtd == 0:
    print("[ ]")


else:
    while cont <= 1:    
        valores = str(input()).split()
        if len(valores) > qtd:
            print(f"tente novamente, você pode passar somente {qtd} valor")
        else:
            print("[ ",end=' ')
            for numero in valores:    
                print(numero, end=' ')
            print(" ]")
            cont += 1