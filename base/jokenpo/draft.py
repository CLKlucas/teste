while True:
    jog1 = str(input().upper())
    jog2 = str(input().upper())

    if (jog1 in "RSP") and (jog2 in "RSP"):
        if jog1 == jog2:
            print("empate")
        elif (jog1 == "R" and jog2 == "S") or (jog1 == "S" and jog2 == "P") or (jog1 == "P" and jog2 == "R"):
            print("jog1")
        else:
            print("jog2")
        break
    
    print("Digite as opções de jogada: R (pedra), P (papel), e S (tesoura).")
