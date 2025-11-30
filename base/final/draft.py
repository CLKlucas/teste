def calculo(primeira_no,segunda_no,final):
    media = (primeira_no + segunda_no) / 2
    if media >= 7:
        return "aprovado"
    elif media >= 4 and media < 7:
        if (media + final) / 2 >= 5:
            return "aprovado pela final"
        else:
            return "reprovado pela final"
    else:
        return "reprovado"    



nota1 = float(input())
nota2 = float(input())
nota_final = float(input())
print(calculo(nota1,nota2,nota_final))
