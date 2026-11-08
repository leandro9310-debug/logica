lista_num = [5, 10, 15, 28, 37, 60]
#Aqui, já entramos a execução do que foi solicitado no descritivo do exercício:
#FUNÇÃO DE SOMA:
def somarmultiplosnumeros(lista_num):
#"def" é o comando para criar uma função
    total = 0
#
    for numero in lista_num:
    #"for" é o comando para repetir uma ação.
    #"in" é o comanod para percorrer os elementos de um lista
        total = total + numero
    return total
#
#FUNÇÃO DE MULTIPLICAÇÃO:
def multiplicarmultiplosnumeros(lista_num):
    total = 1
#
    for numero in lista_num:
        total = total * numero
    return total 
#
#VERIFICAÇÃO SE É OU NÃO PAR:
def ehpar(numero):
    return numero % 2 == 0 and isinstance(numero, int)
# O símbolo % é utilizado para descobrir o resto de uma divisão. Por exemplo: 10/2 = 0, pois 10 dividido por 2 não deixa resto. Já no caso 7/2 = 1, porque 7 dividido por 2 deixa resto 1.
# Se o resto da divisão por 2 for zero, o número é par (desde que seja um número inteiro).
#"and" é o comando para exigir que duas condições sejam verdadeiras.
# O comando "isinstance()" verifica o tipo de um valor.
#
#VERIFICAÇÃO SE É OU NÃO UM NÚMERO INTEIRO:
def ehinteiro(numero):
    return isinstance(numero, int)
#MENSAGEM QUE IRÁ APARECER NO TERMINAL:
numero = 7
print("Lista de números:", lista_num)
#
print("Resultado da soma:", somarmultiplosnumeros(lista_num))
#
print("Resultado da multiplicação:", multiplicarmultiplosnumeros(lista_num))
#
print("O número é par?", ehpar(numero))
#
print("O número é inteiro?", ehinteiro(numero))