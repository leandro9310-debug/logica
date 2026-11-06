from cores import *

tarefas = []

def menu ():
    print("\n" + FRENTE_AMARELO + "__MENU__" + RESET)
    print("1 - Adicionar Tarefas")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefas")
    print("4- Sair")

def adicionarTarefas():
    tarefa = input("Digiti o nome da tarefa: ")
    tarefas.append(tarefa)
    print("Tarefa Adicionada!")

def listarTarefa():
    if len (tarefas) == 0:
        print("Nenhuma tarefa cadastrada")
    else:
        for numero, tarefa in enumerate(tarefa, start=1):
            print(numero, "-", tarefa)

def removerTarefa():
    listarTarefa()

    if len(tarefas) > 0:
        numero =int(input("Digite o númeor da tarefa a remover: "))

        if 1 <= numero <=len (tarefas):
            tarefas.pop(numero - 1)
            print("Tarefa removida")
        else:
            print("Número inválido")

opcao = ""

while opcao != "4":
    menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionarTarefas()
    elif opcao == "2":
        listarTarefa()
    elif opcao == "3":
        removerTarefa()
    elif opcao == "4":
            print("Até Logo")
    else:
        print("Opção inválida!")

menu()