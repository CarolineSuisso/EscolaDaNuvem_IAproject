try:
    n1 = float(input("Digite a primeira nota (N1): "))
    n2 = float(input("Digite a segunda nota (N2): "))
    n3 = float(input("Digite a terceira nota (N3): "))
    n4 = float(input("Digite a quarta nota (N4): "))

    media = ((n1 * 2) + (n2 * 3) + (n3 * 4) + (n4 * 1)) / 10

    print(f"Media: {media:.1f}")

    if media >= 7.0:
        print("Aluno aprovado.")
    elif media < 5.0:
        print("Aluno reprovado.")
    else:
        print("Aluno em exame.")
        
        nota_exame = float(input("Digite a nota do exame: "))
        print(f"Nota do exame: {nota_exame:.1f}")

        media_final = (media + nota_exame) / 2

        if media_final >= 5.0:
            print("Aluno aprovado.")
        else:
            print("Aluno reprovado.")
        
        print(f"Media final: {media_final:.1f}")

except ValueError:
    print("Erro: Por favor, digite apenas valores numéricos para as notas.")