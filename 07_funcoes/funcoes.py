#Função de retorno sem parâmetros
def sobre ():
    print("Desenvolvido por: Leandro Soares")

#Função sem retorno e com parâmetros
def turma(turma):
    print(f"Turma: {turma}")

#Função coiom retorno e com parâmetros
def somar (numero1, numero2):
    return numero1 + numero2

sobre()
turma("AD-05")

resultado = somar (10, 5)
print(f"A soma de 10 + 5 = {resultado}")