from time import sleep
from random import randrange
rodadas = 1
chances = 0
secret = randrange(10,1000)

print("QUAL É O NÍVEL DE DIFICULDADE?")
print("[1] FÁCIL")
print("[2] MEDIA")
print("[3] DIFÍCIL")
nivel = int(input("DEFINA O NÍVEL:"))
niveis = int(nivel)
if (nivel == 1):
    chances = 20
elif (nivel == 2):
    chances = 10
else:
    chances = 5
for rodadas in range(1, chances + 1):
    print("TENTATIVAS: {} de {}".format(rodadas,chances))
    chutes = str(input("INFORME UM NUMERO ENTRE 1 E 1000:")).strip()
    chute = int(chutes)
    if (chute < 10 or chute > 1000):
        print("VOCÊ DEVE DIGITAR UM NÚMERO ENTRE 10 E 1000!")
        continue
    print("PROCESSING...")
    sleep(3)
    if (secret == chute):
        print("VOCÊ ACERTOU")
        break
    else:
        if (chute > secret):
                print("VOCE ERRROUUU! O SEU CHUTE FOI MAIOR.")
        elif (chute < secret):
            print("VOCE ERRROUUU ! SEU CHUTE FOI MENOR .")
            rodadas = rodadas + 1

print("GAME OVER")
