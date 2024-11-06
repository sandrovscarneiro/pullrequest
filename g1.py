import random

def jogo_adivinhacao():
    numero_secreto = 0 #REMOVA O 0 E COMPLETE O CÓDIGO A FIM DE COMPLETAR O JOGO DE ADIVINHAÇÃO
    tentativas = 0
    print("Bem-vindo ao jogo de adivinhação!")
    print("Tente adivinhar o número entre 1 e 100.")

    while True:
        palpite = int(input("Digite seu palpite: "))
        tentativas += 1

        if palpite < numero_secreto:
            print("Muito baixo! Tente novamente.")
        elif palpite > numero_secreto:
            print("Muito alto! Tente novamente.")
        else:
            print(f"Parabéns! Você adivinhou o número {numero_secreto} em {tentativas} tentativas.")
            break

jogo_adivinhacao()
