semana = int(input())
horario = int(input())

if semana > 1 and semana <= 7:
    if semana == 7:
        if horario >= 8 and horario <= 11:
            print("SIM")
        else:
            print("NAO")
    else:
        if (horario >= 8 and horario <= 11) or (horario >= 14 and horario <= 17):
            print("SIM")
        else:
            print("NAO")                 
else:
    print("NAO")
