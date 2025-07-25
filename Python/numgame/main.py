import calculadora as calc
import numalet as nl
import time
import game

'''
Jogo/programa de juntar outros programas
A ideia é definir funções em outros programas e usa-las aqui

Como funciona:
    O jogo gerará nums de 1 a 100 e então lhe dara uma meta
    Além disso te dará 3 dicas aleatórias que você pode pedir
    No fim, deve dizer se é possivel atingir a meta com uma operação mat
    Se for possivel, com qual então
'''

def gerarNums():
    print("Gerando os números")
    a = nl.gerarNum(); b = nl.gerarNum()
    time.sleep(3)
    print("Números gerados")
    return a, b

def gerarCond():
    print('Gerando condição')
    time.sleep(2)

    #criar 5(1 maior; 2 menor; entre x1/x1; entre 0/1; res negativo)
    a = nl.gerarNum0()
    x1 = nl.gerarNum(); x2 = nl.gerarNum()
    lin = "Sua condição é: "

    if a < 20:
        cond = 1
        print(lin+"resultado menor que "+str(x1))
    elif a == 20 or a > 40:
        cond = 2
        print(lin+"resultado maior que "+str(x1))
    elif a == 40 or a > 60:
        cond = 3
        print(lin+"resultado entre "+str(x1)+" e "+str(x2))
    elif a == 60 or a > 80:
        cond = 4
        print(lin+"resultado entre 0 e 1")
    else:
        cond = 5
        print(lin+"resultado negativo")
    
    return cond, x1, x2

def iniciarGame(): 
    print("Jogo de acertar a condição com números =D")

    print("")
    a, b = gerarNums()

    print("")
    cond, x1, x2 = gerarCond()

    print("")
    game.carregarDicas(a, b)
    time.sleep(2)

    print("")
    game.iniciarCalcu(a, b, cond, x1, x2)

    print("Se quiser tentar de novo, reinicie o programa!")
    time.sleep(3)

iniciarGame()