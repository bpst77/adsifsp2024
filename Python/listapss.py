import time
'''
Programa para cadastrar pessoas e exibir no fim, a mais velha e a média da idade

estrutura pensada
1 - cadastrar 1 pessoa(obrigatório)
2 - perguntar se quer cadastrar mais
3 - mostrar dados
'''

def addPessoa(lista):
    print("Cadastrando pessoas")
    time.sleep(2)

    resp = True
    while resp == True:
        print("Adicionando uma pessoa")
        nom = input("Digite o nome: ")
        idd = int(input("Digite a idade: "))
        x = {"nome": nom, "idade": idd}
        lista.append(x.copy())
        print("Pessoa adicionada")
        time.sleep(2)

        print("")
        resp = input("Adicionar mais uma pessoa? (s/n): ").lower()
        
        if resp == 's':
            resp = True

    return lista

def mostrarDados(lista):
    print("Processando")
    med = 0
    maisVelho = {}

    for i in lista:
        med = med + i["idade"]

        if not maisVelho:
            maisVelho = i
        elif maisVelho["idade"] < i["idade"]:
            maisVelho = i
    time.sleep(2)

    med = med/len(lista)
    print("Processamento feito!")
    time.sleep(2)

    print("")
    print("Média de idade das pessoas cadastradas: "+str(med))
    print("Pessoa mais velha cadastrada: "+maisVelho["nome"])

def Iniciar():
    lista = []

    print("Programa de cadastro de pessoas")
    time.sleep(2)

    print("")
    lista = addPessoa(lista)

    print("")
    mostrarDados(lista)

Iniciar()