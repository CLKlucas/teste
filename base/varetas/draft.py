vareta1 = int(input())
vareta2 = int(input())
vareta3 = int(input())


if (vareta1 < vareta2 + vareta3) and (vareta2 < vareta1 + vareta3) and (vareta3 < vareta1 + vareta2):
    print(True)
else:
    print(False)
                 