#IMPORTAÇÃO DE ELEMENTOS DE CORES QUE ESTÃO EM OUTRO ARQUIVO:
from cores import *
#"from" é o comando que indica onde iremos buscar determinadas ferramentas.
#"import" é o comando para importamos uma caixa de ferramentas com várias ferramentas prontas. Em vez de construir todas novamente, pode importar ferramentas de outro arquivo.
#"*" é o comando que significa a importação de todos os nomes disponíveis nesse módulo.
#CRIANDO UMA VÁVIAVEL PARA CRIAR UM LISTA VAZIA PARA GUARDAR AS TAREFAS:
tarefas = []
#FUNÇÃO PARA MOSTRAR O MENU:
def menu ():
    print("\n" + FRENTE_AMARELO + "__MENU__" + RESET)
    #"\n" é um comando que representa uma quebra de linha.
    #"+" Quando utilizado entre textos (strings), ele pode juntar esses textos.
    print("1 - Adicionar Tarefas")
    print("2 - Listar Tarefas")
    print("3 - Remover Tarefas")
    print("4- Sair")
#FUNÇÃO PARA ADICIONAR TAREFAS:
def adicionarTarefas():
    tarefa = input("Digiti o nome da tarefa: ")
    tarefas.append(tarefa)
    #O "append()"" serve para adicionar um elemento ao final de uma lista.
    print("Tarefa Adicionada!")
#FUNÇÃÕ PARA LISTAR TAREFAS:
def listarTarefa():
    if len (tarefas) == 0:
        #"len()" é o comando que irá conta quantos elementos existem dentro de uma lista.
        print("Nenhuma tarefa cadastrada")
    else:
        for numero, tarefa in enumerate(tarefas, start=1):
            #"enumerate()" é o comando merece atenção especial. Ele percorrer uma lista e obtem as informações: 1 - A posição do elemento e 2 - O próprio elemento.
            #"start=1" é o comando que determina que a numeração comece em 1.
            print(numero, "-", tarefa)
#FUNÇÃO PARA REMOVER TAREFAS:
def removerTarefa():
    #Esse primeiro mostra todas as tarefas cadastradas:
    listarTarefa()
    #Próxima linha verifica se existe alguma tarefa na lista:
    if len(tarefas) > 0:
        numero =int(input("Digite o númeor da tarefa a remover: "))
        #Próxima linha verifica se o número está dentro dos limites da lista:
        if 1 <= numero <=len (tarefas):
        #"len" conta quantos elementos existem dentro de uma lista.
            tarefas.pop(numero - 1)
            #".pop" é o comando que remove um elemento da lista pela sua posição (índice).
            print("Tarefa removida")
        else:
            print("Número inválido")
#INÍCIO DA EXECUÇÃO DO PROGRAMA:
opcao = ""
# Continua repetindo enquanto a opção for diferente de 4:
while opcao != "4":
#"while" é o comando que irá repetir uma ação enquanto determinada condição for verdadeira.
    menu()
    opcao = input("Escolha uma opção: ")
#
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