import random

def jogar_adivinhacao():

    print("*********************************")
    print("Bem vindo ao jogo de Adivinhação!")
    print("*********************************")

    numero_secreto = random.randrange(1,101) #o range vai de 0 ateh 100 - o ultimo numero não é incluso
    total_de_tentativas = 0
    pontos = 1000

    print("Qual o nível de dificuldade?")
    print("(1) Fácil (2) Médio (3) Difícil")

    nivel = int(input("Defina um nível: ")) #input sempre entra como str, por isso precisa converter para int

    if(nivel == 1):
        total_de_tentativas = 20
    elif (nivel == 2):
        total_de_tentativas = 10
    else:
        total_de_tentativas = 5

    # print(numero_secreto)

    for rodada in  range (1, total_de_tentativas+1):
        print("Tentativa {} de {}".format(rodada, total_de_tentativas))
        chute_str = input("Digite um número entre 1 e 100: ")
        print("Você digitou ", chute_str)
        chute = int(chute_str)

        if(chute < 1 or chute > 100):
            print("Você deve digitar um número entre 1 e 100!")
            continue


        acertou = chute == numero_secreto
        maior = chute > numero_secreto
        menor = chute < numero_secreto

        if (acertou):
            print("Você acertou e fez {} pontos!".format(pontos))
            break
        else:
            if(maior):
                print("Você errou! Seu chute foi maior que número secreto.\n")
                if(rodada == total_de_tentativas):
                    print()
            elif(menor):
                print("Você errou! Seu chute foi menor que número secreto.\n")
            pontos_perdidos = abs(numero_secreto - chute) #tem que ser sempre o número absoluto, ou seja, não importa se é negativo ou positivo
            pontos = pontos - pontos_perdidos

    print("Fim de jogo!")

if(__name__== "__main__"):   #pra mostrar qual é o arquivo principal
    jogar_adivinhacao()