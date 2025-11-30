def firewall(internet,autenticacao,administrador):
    if (not internet):
        return "you must connect to wifi" 
    elif (not autenticacao):
        return "you need to login first"
    elif (not administrador):
        return "you must login as admin"
    return "done"


wifi = int(input())
login = int(input())
admin = int(input())

print(firewall(wifi,login,admin))