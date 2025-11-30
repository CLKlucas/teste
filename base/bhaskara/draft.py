import math

def bhaskara(a,b,c):
    delta = math.sqrt(valor_B**2 - 4 * valor_A * valor_C)

    bhaskara_positiva = (-valor_B + delta) / (2*valor_A)
    
    if delta > 0:
        bhaskara_negativa = (-valor_B - delta) / (2*valor_A)
        print(f"{bhaskara_positiva:.2f}")
        print(f"{bhaskara_negativa:.2f}")

    elif delta == 0:
        print(f"{bhaskara_positiva:.2f}")    

    else:   
        print("nao ha raiz real")


valor_A = float(input())
valor_B = float(input())
valor_C = float(input())

bhaskara(valor_A,valor_B,valor_C)