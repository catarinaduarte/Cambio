"""
Conversor cambial EUR<->USD. Exibe um menu com as seguintes opções:

    Escolha o sentido da conversao
    1. Euros -> Dolares
    2. Dólares -> Euros
    > 1
    Montante em euros: 10
    12.223
    Deseja repetir? (S/N) ds
    Opção <ds> inválida.
    Deseja repetir? (S/N)

Nesta versão o câmbio é fixo.
"""

import sys
import subprocess
from decimal import Decimal as dec

cambio = dec('1.2223')  # 1 euro compra 1.1077 dólares (preço do EURO em USD)

def confirma(msg):
    while True:
        opcao_repetir = input(msg).upper()
        if opcao_repetir in ('S', 'SIM'):
            return True
        elif opcao_repetir in ('N', 'NAO', 'NO'):
            return False
        else:
            print(f'Opção <{opcao_repetir}> inválida')

def cls():
    if sys.platform in ('darwin', 'linux', 'unix', 'bsd'):
        subprocess.run(['clear'], check=True)
    elif sys.platform == 'win32':
        subprocess.run(['cls'], shell=True, check=True)

def pause(msg='Pressione ENTER p/ continuar....'):
    input(msg)

repetir_conversao = True
while repetir_conversao:
    # 1. Exibir as opções do menu
    cls()
    print("Escolha o sentido da conversao")
    print("1. Euros -> Dólares")
    print("2. Dólares -> Euros")

    # 2. Ler a opção
    opcao = input("> ")
    print()

    # 3. Executar a opção
    if opcao == '1':
        montante = dec(input("Montante em euros: "))
        print(f"Dólares -> {montante * cambio:.2f}")
    elif opcao == '2':
        montante = dec(input("Montante em dólares: "))
        print(f"Euros -> {montante / cambio:.2f}")
    else:
        pause(f"Opção <{opcao}> inválida! Pressione ENTER p/ continuar... ")
        continue

    print()

    # 4. Repetir ou terminar
    repetir_conversao = confirma("Deseja repetir conversão? (S/N) ")

    # ALTERNATIVA:
    #
    # while True:
    #   # 1.
    #   # 2.
    #   # 3.
    #   # 4. Repetir ou terminar
    #   if not confirma("Deseja repetir conversão? (S/N) "):
    #      break


