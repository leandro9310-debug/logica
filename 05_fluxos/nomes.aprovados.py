nomes_aprovados = ["João", "Maria", "Pedro", "Mariana"]

nome = input ("Digite o seu nome: ").strip()

if nome.lower() in [n.lower() for n in nomes_aprovados]:
    print(f"{nome} aprovado(a)!")
else:
    print(f"{nome} reprovado(a)!")