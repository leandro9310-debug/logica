nome=input("Digite o nome do aluno: ")
nota1=float(input("Digite a primeira nota: "))
nota2=float(input("Digite a segunda nota: "))

media=(nota1 + nota2 ) / 2

if media >= 7:
    print(f"{nome} foi APROVADO(A) com a média {media}!")
elif media >= 5:
    print(f"{nome} está de Exame com a média {media}.")
else:
    print(f"{nome} foi REPROVADO (A) com a média {media}")
