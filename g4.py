import math

def calcular_fatorial():
    numero = int(input("Digite um número inteiro positivo: "))
    
    if numero < 0:
        print("Por favor, insira um número inteiro positivo:")
    else:
        fatorial = 0 #REMOVA O 0 E COMPLETE A VARIÁVEL A FIM DE CALCULAR O FATORIAL DO NÚMERO
        print(f"O fatorial de {numero} é: {fatorial}")

calcular_fatorial()
