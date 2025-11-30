def round(numero):
    part_frac = numero % 1
    if part_frac >= 0.5:
         para_cima = 1 - part_frac
         numero = numero + para_cima
         return numero
    else:
        numero = numero - part_frac
        return numero 
        
     
def ceil(numero):
    part_frac = numero % 1
    para_cima = 1 - part_frac
    numero = numero + para_cima
    return numero


def floor(numero):
    part_frac = numero % 1
    numero = numero - part_frac
    return numero 



operacao = str(input())
num = float(input())

if operacao == "r":
    print(f"{round(num):.0f}")
elif operacao == "c":
    print(f"{ceil(num):.0f}")
else:
    print(f"{floor(num):.0f}")                