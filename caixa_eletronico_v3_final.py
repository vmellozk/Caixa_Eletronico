from time import sleep
import random
from collections import Counter
import os
import logging

logging.basicConfig(filename='caixa.log', level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def limpar_console():
    os.system("cls" if os.name == 'nt' else 'clear')        #os.name == 'nt' vai verificar se é windows, e ai vai utilizar o cls, se não, usa-se o clear

def realizar_saque():
    logging.info("Início do saque:")
    print("\nBEM VINDO AO SAQUE RÁPIDO!")
    sleep(1)

    valoresDisponiveis = [1, 10, 20, 50]

    print("NOTAS DISPONÍVEIS: R$1, R$10, R$20 e R$50")
    sleep(1)
    print("(valor mínimo: R$20)")
    sleep(4)

    limpar_console()
    
    while True:
        try:
            saque = int(input("\nQual valor você quer sacar? "))
            if saque <=0:
                logging.error("Valor abaixo do permitido.")
                print("Por favor, insira um valor positivo.")
            else:
                break        #retorna o valor se for válido, se for inteiro
        except ValueError:
            print("Por favor, insira um valor válido.")


    somaAtual = 0
    notasUtilizadas = []                                        #criado para armazenar o valor das notas utilizadas

    while somaAtual < saque:
        numeroAleatorio = random.choice(valoresDisponiveis)     #choice utilizado para retornar um elemento aleatório
        if somaAtual + numeroAleatorio <= saque:                # condição de controle para o valor não exceder o saque
            somaAtual += numeroAleatorio
            notasUtilizadas.append(numeroAleatorio)
            if saque < 20:
                print("Valor muito baixo, não podemos realizar esse saque! Tente novamente.")
                saque = int(input("\nQual o valor você quer sacar? "))

    limpar_console()

    sleep(1)
    print("OK, Verificando...")
    sleep(2)
    print("Valor disponível! Contando...")
    sleep(2)

    limpar_console()

    print(f"\nSaque de R${somaAtual} realizado! Contém: ")
    contador_notas = Counter(notasUtilizadas)               # Convertendo a lista para um objeto Counter para contar as ocorrências de cada valor

    for nota, quantidade in contador_notas.items():         # Iterando sobre o contador e mostrando a quantidade de cada nota utilizada
        print(f"{quantidade} nota(s) de R${nota}.")

    sleep(1)
    print("\nRETIRE SEU DINHEIRO!")
    sleep(6)

    limpar_console()

    logging.info("Saque realizado.")

while True:
    realizar_saque()

    saque_novamente = input("\nGOSTARIA DE REALIZAR OUTRO SAQUE? [S] para SIM ou [N] para não: ")
    limpar_console()
    if saque_novamente not in 'Ss':
        print("OK, fechando o caixa!")
        print("Obrigado por utilizar o nosso serviço, volte sempre!")
        logging.info("Fechamento do caixa.")
        break