

alfabeto = "abcdefghijklmnopqrstuvwxyz"


soma = int(input())
if soma <= 0 or soma >= 100:
    print("Joguem de novo")    
else:
    if soma > 26:
        soma = soma % 26   
       
    print(alfabeto[soma - 1])
            