def mumia(name,age):
    if age < 12:
        return print(f"{name} eh crianca")
    elif age < 18:
        return print(f"{name} eh jovem")
    elif age < 65:
        return print(f"{name} eh adulto")
    elif age < 1000:
        return print(f"{name} eh idoso")
    else: 
        return print(f"{name} eh mumia")



nome = str(input())
idade = int(input())
mumia(nome,idade)