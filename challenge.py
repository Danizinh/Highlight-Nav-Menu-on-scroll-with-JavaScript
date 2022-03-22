count = 0
option = ""
from random import randint
from time import sleep
while option !="n":
    computer = randint(10,1000)
    print('-=-' * 20)
    print('I WILL THINK OF A NUMBER BETWEEN 10 AND 1000. TRY TO GUESS...')
    print('-=-' * 20)
    jogador = int(input("WHAT NUMBER DID I THINK ABOUT?"))
    print("PROCESSING...")
    sleep(2)
    if jogador == computer:
        print("WOOOOOOOOOOOOOOOO YOU MADE ME!")
    else:
        print(f"WON! I THOUGHT ABOUT THE NUMBER {computer} AND NO {jogador}!")
    opcao = str(input("DO YOU WANT TO TRY AGAIN [S/N]?"))


