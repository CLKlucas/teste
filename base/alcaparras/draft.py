frase = str(input())
palavra = str(input())
cont = 0
for i in range(len(frase)):
    if palavra == frase[i]:
        cont += 1
print(cont)        