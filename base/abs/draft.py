
def absoluto(numero1,numero2):
    calculo = num1 - num2
    if calculo < 0:
        calculo = calculo * -1
    return calculo    


num1 = int(input())
num2 = int(input())

print(absoluto(num1,num2))


