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

def inteiro(numero):
    if isinstance(numero, bool):
        return False
    if isinstance(numero, int):
        return True
    if isinstance(numero, float):
        return numero.is_integer()

def par(numero):
    if not ehinteiro(numero):
        return False

    return num % 2 == 0


if __name__ == "__main__":

    print("Soma [5, 10, 15]:",
          somarmultiplosnumeros([5, 10, 15]))

    print("Soma [0.5, -4, 2]:",
          somarmultiplosnumeros([0.5, -4, 2]))

    print("Multiplicação [2, 5]:",
          multiplicarmultiplosnumeros([2, 5]))

    print("Multiplicação [-1, 3, 2.5]:",
          multiplicarmultiplosnumeros([-1, 3, 2.5]))

    print("ehpar:", ehpar(8))
    print("ehpar:", ehpar(5))
    print("ehpar:", ehpar(2))

    print("É inteiro:", ehinteiro(5))
    print("É inteiro:", ehinteiro(5.5))
    print("É inteiro:", ehinteiro(8.0))
