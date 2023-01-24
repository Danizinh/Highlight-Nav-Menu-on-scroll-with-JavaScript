count = 0
option = ""
from random import randint
from time import sleep
while option !="n":
    computer = randint(10,1000)
    print('-=-' * 20)
    print('VOU PENSAR EM UM NÚMERO ENTRE 10 E 1000. TENTE ADIVINHAR....')
    print('-=-' * 20)
    jogador = int(input("EM QUE NÚMERO EU PENSEI?"))
    print("PROCESSING...")
    sleep(2)
    if jogador == computer:
        print("WOOOOOOOOOOOOOOOO VOCÊ ME FEZ!")
    else:
        print(f"WON! EU PENSEI NO NÚMERO {computer} E NÃO{jogador}!")
    opcao = str(input("VOCÊ QUER TENTAR DE NOVO [S/N] ?"))
