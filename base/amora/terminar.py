frase = str(input())
palavra = str(input())
nova_frase =""
cont = 0

print(palavra[0])

for frs in range(len(frase) + 1):
    if frs + 1 == len(frase):
        break
    
    for plv in range(len(palavra)):
        
        if palavra[plv] == frase[frs]:
            nova_frase += frase[frs]
            break

        if nova_frase == palavra:
            print("contando")
            cont += 1
            nova_frase = ""
print(cont)        