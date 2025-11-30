def calculadora(num1,num2,matematica):
    if (matematica == "+"):
        print (num1 + num2)
    elif (matematica == "-"):
        print (num1 - num2)
    elif (matematica == "*"):
        print (num1 * num2)
    else:
        print (num1 // num2)



numero1 = int(input())
numero2 = int(input())
operacao = str(input())

calculadora(numero1,numero2,operacao)