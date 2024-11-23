import random

def jogo ():

    numero = random.randint(1,5)
    vida = 3

    print ("Advinhe o número entre 1 e 5\n")

    while vida > 0: 
        print ("Você tem", vida, "vidas.\n")
        palpite = int (input ("Qual é o número?: "))
        print ()

        if palpite == numero:
            print ("Parabéns! Você Ganhou! O número era: ", numero)

            resposta = input ("Você quer jogar novamente? (s/n): ").lower()
            print ()

            if resposta == 's':
                jogo ()
            elif resposta == 'n':
                print ("Obrigado por jogar :)")
                break

        
        else:
            vida -= 1
            if vida > 0:
                print ("Você errou, tente de novo!!")
            else:
                print ("Vidas zeradas, fim de jogo!!")

jogo()