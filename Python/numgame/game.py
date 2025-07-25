import calculadora as calc
import numalet as nl
import time

def umnDicas(resp, a, b):
    x3 = x3 = nl.gerarNum()

    if (resp == 1):
        c = a
        d = b
        lin = "O primeiro número "
        lin2 = "é maior que o segundo"
        lin3 = "não é maior que o segundo"
    elif (resp == 2):
        c = b
        d = a
        lin = "O segundo número "
        lin2 = "é maior que o primeiro"
        lin3 = "não é maior que o primeiro"
    
    if x3 < 50:
        if c > d:
            lin = lin + lin2
        else:
            lin = lin + lin3
    else:
        if c >= 20:
            lin = lin + "está entre 0 e 20"
        elif c >= 40:
            lin = lin + "está entre 20 e 40"
        elif c >= 60:
            lin = lin + "está entre 40 e 60"
        elif c >= 80:
            lin = lin + "está entre 60 e 80"
        else:
            lin = lin + "está entre 80 e 100"
    
    print(lin)

def carregarDicas(a, b):
    print("Parte das dicas!")
    time.sleep(2)

    n = 3 #dicas
    print("Você pode escolher 3 dicas e elas serão aleatórias")
    time.sleep(2)
    print("\nDicas:")
    print("1) Sobre o 1 número")
    print("2) Sobre o 2 número")
    print("3) Sobre ambos(mais abrangente)")
    print("OBS: a ordem dos números importa")
    resp = int(input("Qual vai ser? : "))

    print("\nOk, sua dica é")
    #tipos de dicas: 1 e 2) maior/menor e entre; 3)soma e subtração do dobro

    while n != 0:
        match resp:
            case 1:
                umnDicas(resp, a, b)
            case 2:
                umnDicas(resp, a, b)
            case 3:
                x3 = nl.gerarNum()
                if x3 < 50:
                    x4 = (a*2)+(b*2)
                    print("A soma do dobro dos dois números é "+str(x4))
                else:
                    x4 = (a*2)-(b*2)
                    if x4 <= 0:
                        print("A subtração do dobro dos dois números é menor ou igual a 0")
                    else: 
                        print("A subtração do dobro dos dois números é "+str(x4))
        if n != 1:
            resp = int(input("\nOk, próximo: "))
        n = n-1
    return

def checarCond(a, b, cond, x1, x2):
    n = 1
    resp2 = 2

    while (resp2 == False) or (n != 6):
        match n:
            case 1:
                res = calc.multiplicar(a, b)
            case 2:
                res = calc.dividir(a, b)
            case 3:
                res = calc.somar(a, b)
            case 4:
                res = calc.subtrair(a, b)

        match cond:
            case 1:
                c = res < x1
            case 2:
                c = res > x1
            case 3:
                c = (res >= x1 and res <= x2) or (res >= x2 and res <= x1)
            case 4:
                c = res >= 0 and res <= 1
            case 5:
                c = res < 0

        if c:
            resp2 = True
          
        n = n+1

    return resp2

def confCond(res, resp2, cond, x1, x2):
    match cond:
        case 1:
            if res < x1:
                resp2 = True
            else:
                resp2 = False
        case 2:
            if res > x1:
                resp2 = True
            else:
                resp2 = False
        case 3:
            if (res >= x1 and res <= x2) or (res >= x2 and res <= x1):
                resp2 = True
            else:
                resp2 = False
        case 4:
            if (res >= 0 and res <= 1):
                resp2 = True
            else:
                resp2 = False
        case 5:
            if (res > 0):
                resp2 = True
            else:
                resp2 = False
    return resp2

def iniciarCalcu(a, b, cond, x1, x2):
    print("Parte da calculadora")
    print("Agora, você deve dizer se é possivel atender a condição com uma das quatro operações")
    resp = input("E então, é possivel? (s / n)")
    if resp == 's':
        resp = True
    else:
        resp = False

    print("\nChecando resposta...")
    time.sleep(2)

    resp2 = False
    match cond:
        case 1:
            resp2 = checarCond(a, b, cond, x1, x2)
        
        case 2:
            resp2 = checarCond(a, b, cond, x1, x2)

        case 3:
            resp2 = checarCond(a, b, cond, x1, x2)

        case 4:
            resp2 = checarCond(a, b, cond, x1, x2)

        case 5:
            resp2 = checarCond(a, b, cond, x1, x2)

    if resp == resp2:
        if resp == False:
            print('\nOk, vejamos...')
            time.sleep(2)
            print('...')
            time.sleep(2)
            print('...')

            print("\nCorreto")
            print("Parabéns, você venceu!")
        else:
            print('\nOk, vejamos...')
            time.sleep(2)
            print('...')
            time.sleep(2)
            print('...')

            print("Correto")
            print("Agora, você deve dizer uma operação que atende a condicao")
            print("\nLista de operacoes:")
            print("1) multiplacacao; 2) divisao")
            print("3) adicao; 2) subtracao")

            resp = int(input('Qual operação você acha que serve? :'))
            match resp:
                case 1:
                    res = calc.multiplicar(a, b)

                    resp2 = confCond(res, resp2, cond, x1, x2)
                case 2:
                    res = calc.dividir(a, b)

                    resp2 = confCond(res, resp2, cond, x1, x2)
                case 3:
                    res = calc.somar(a, b)

                    resp2 = confCond(res, resp2, cond, x1, x2)
                case 4:
                    res = calc.subtrair(a, b)

                    resp2 = confCond(res, resp2, cond, x1, x2)

            if resp2 == False:
                print('\nOk, vejamos...')
                time.sleep(2)
                print('...')
                time.sleep(2)
                print('...')
                print("\nOh no, parece que você errou")
                print("Mais sorte da proxima vez")
            else:
                print('\nOk, vejamos...')
                time.sleep(2)
                print('...')
                time.sleep(2)
                print('...')
                print("\nCorreto")
                print("Parabéns, você venceu!")
    else:
        print('\nOk, vejamos...')
        time.sleep(2)
        print('...')
        time.sleep(2)
        print('...')
        print("\nOh no, parece que você errou")
        print("Mais sorte da proxima vez")