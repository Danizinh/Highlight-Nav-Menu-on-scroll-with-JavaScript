count = 0
opcao = ""
from random import randint
from time import sleep
while opcao !="n":
    computer = randint(10,1000)
    print('-=-' * 20)
    print('VOU PENSAR EM UM NUMERO ENTRE 10 e 1000. TENTE ADIVINHAR...')
    print('-=-' * 20)
    jogador = int(input("EM QUE NUMERO EU PENSEI?"))
    print("PROCESSANDO...")
    sleep(2)
    if jogador == computer:
        print("UAUUUUUUUUUU VOCE CONSEGUIU ME VENCER!")
    else:
        print(f"GANHEI! PENSEI NO NUMERO {computer} E NAO NO {jogador}!")
    opcao = str(input("VOCÊ DESEJA TENTAR OUTRA VEZ [s/n]?"))


