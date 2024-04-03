from time import sleep
import random
from collections import Counter
import os

def limpar_console():
    os.system("cls" if os.name == 'nt' else 'clear')

print("\nBEM VINDO AO SAQUE RÁPIDO!")
sleep(1)
valoresDisponiveis = [1, 10, 20, 50]
print("NOTAS DISPONÍVEIS: R$1, R$10, R$20 e R$50")
sleep(1)

while True:
    limpar_console()
    saque = int(input("\nQual valor você quer sacar? "))
    limpar_console()
    print("OK, Verificando...")
    sleep(2)
    print("Valor disponível! Contando...")
    sleep(2)
    limpar_console()

    somaAtual = 0
    notasUtilizadas = []

    while somaAtual < saque:
        numeroAleatorio = random.choice(valoresDisponiveis)
        if somaAtual + numeroAleatorio <= saque:
            somaAtual += numeroAleatorio
            notasUtilizadas.append(numeroAleatorio)
            if saque < 20:
                print("Valor muito baixo, não podemos realizar esse saque! Tente novamente.")
                sleep(2)
                limpar_console()
                continue

    contador_notas = Counter(notasUtilizadas)
    print(f"\nSaque de R${somaAtual} realizado! Contém: ")
    for nota, quantidade in contador_notas.items():
        print(f"{quantidade} nota(s) de R${nota}.")
    sleep(1)
    print("\nRETIRE SEU DINHEIRO!")
    saque_novamente = input("GOSTARIA DE REALIZAR OUTRO SAQUE? [S] para SIM ou [N] para não: ")
    if saque_novamente in 'Ss':
        continue
    else:
        print("OK, fechando o caixa!")
        print("Obrigado por utilizar o nosso serviço, volte sempre!")
        break
