from time import sleep
import random

print("\nCAIXA ELETRÔNICO")
sleep(1)

valoresDisponiveis = [1, 10, 20, 50]

print("PARA SAQUE, APENAS NOTAS DE:", end="")
print(" R$1, R$10, R$20 e R$50")
sleep(2)

saque = int(input("\nQual valor você quer sacar? "))

somaAtual = 0
notasUtilizadas = []                                        #criado para armazenar o valor das notas utilizadas
while somaAtual < saque:
    numeroAleatorio = random.choice(valoresDisponiveis)     #choice utilizado para retornar um elemento aleatório
    if somaAtual + numeroAleatorio <= saque:                # condição de controle para o valor não exceder o saque
        somaAtual += numeroAleatorio
        notasUtilizadas.append(numeroAleatorio)

print(f"\nSaque de R${somaAtual}")
print(f"Foram utilizadas as seguintes notas: {notasUtilizadas}")