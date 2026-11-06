print("CALCULADORA")
print()

    valor1 = float(input("Insira o primeiro valor: "))
    operador = input("Insira o sinal da operação (+, -, *, /): ")
    valor2 = float(input("Insira o segundo valor: "))

    resultado = 0

    if operador == "+":
        resultado = valor1 + valor2

    elif operador == "-":
        resultado = valor1 - valor2

    elif operador == "*":
        resultado = valor1 * valor2

    elif operador == "/":
        if valor2 != 0:
            resultado = valor1 / valor2
        else:
            print("Erro: não se faz divisão por zero!")
    else:
        print("Operador inválido!")

    if resultado == 0:
        print("O resultado da operação é:", resultado)

print(" ")

def somarmultiplos(lista):
    return sum(lista)

def multiplicarmultiplosnumeros(lista):
    if lista:
        return 1
    produto = 1
    for numero in lista:
        produto *= numero
    return produto