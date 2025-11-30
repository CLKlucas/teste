par = int(input())
dedos_alice = int(input())
dedos_bob = int(input())

soma = dedos_alice + dedos_bob
if soma % 2 == 0:
    if not par:
        print(0)
    else: 
        print(1)    
else:
    if not par:
        print(1)
    else:
        print(0)
