import random
import os


#cores ansi
class colors:
    cyan = '\033[1;36m'
    white = '\033[1;97m'
    yellow = '\033[1;33m'
    end = '\033[0m'
    green = '\033[92m'
    red = '\033[91m'
#definindo funções
def finalizar_programa():
    print(colors.red + 'Finalizando programa...' + colors.end)
    exit()

def limpar_terminal():
    os.system('cls' if os.name == 'nt' else 'clear')

def gerar_numero_aleatorio():
    print(colors.yellow + 'Gerando número aleatório entre 1 e 100...' + colors.end)
    numero_aleatorio = random.randrange(101)
    return numero_aleatorio

limpar_terminal()

#Apertar enter para continuar
print(colors.white + '''\n----------------------------- Bem-vindo! -----------------------------\n''' + colors.end)
while True:
    devo_começar = input('Pressione ENTER para começar...')
    if devo_começar == '':
        break
    else:
        finalizar_programa()


numero_gerado = gerar_numero_aleatorio()


while True:
    try:
        resposta = int(input('Qual número foi gerado? '))
        if resposta == numero_gerado:
            print(colors.green + f'Parabéns! Você acertou o número! o valor gerado foi: {resposta}.' + colors.end)
            jogar_novamente = input('Deseja jogar novamente? (s/n): ')
            if jogar_novamente.lower() == 'n' or jogar_novamente.lower() == 'não':
                finalizar_programa()
            elif jogar_novamente.lower() == 's' or jogar_novamente.lower() == 'sim':
                limpar_terminal()
                numero_gerado = gerar_numero_aleatorio()
                continue
            else:
                print(colors.yellow +'Resposta inválida!' + colors.end)
                finalizar_programa()
        elif resposta > numero_gerado:
            print('Chute um número \033[1;36mmenor!\033[m')
        elif resposta < numero_gerado:
            print('Chute um número \033[1;36mmaior!\033[m')
    except ValueError:
        print(colors.red +'Por favor digite um número de valor inteiro!' + colors.end)