from primeiro import registrar_numero, converter_binario, converter_decimal, soma_binario, subtrair_binario, multiplicar_binario, dividir_binario
from matriz import criar_matriz, operar_matrizes  # Importa as funções necessárias


def menu_principal():
    print("=" * 45)
    print(f"{'MENU PRINCIPAL':^45}")
    print("=" * 45)
    print(f"{'1':<10}{'BINÁRIO':<30}====|")
    print(f"{'2':<10}{'MATRIZ':<30}====|")
    print(f"{'3':<10}{'SAIR':<30}====|")
    print("=" * 45)


def menu_MATRIZ():
    print("=" * 45)
    print(f"{'CALCULADORA DE MATRIZES':^40}====|")
    print("=" * 45)
    print(f"{'1':<10}{'Criar matrizes':<30}====|")
    print(f"{'2':<10}{'Somar matrizes':<30}====|")
    print(f"{'3':<10}{'Subtrair matrizes':<30}====|")
    print(f"{'4':<10}{'Multiplicar matrizes':<30}====|")
    print(f"{'5':<10}{'Determinante da matriz':<30}====|")
    print(f"ww{'6':<10}{'Inversa da matriz':<30}====|")
    print(f"{'7':<10}{'Matriz transposta':<30}====|")
    print(f"{'8':<10}{'Voltar ao menu principal':<30}====|")
    print("=" * 45)


def menu_BINARIO():
    print("=" * 45)
    print(f"|===={'CALCULADORA DE BINÁRIOS':^35}====|")
    print("=" * 45)
    print('1 - Converter decimal para binário')
    print('2 - Converter binário para decimal')
    print('3 - Soma de números binários')
    print('4 - Subtração de números binários')
    print('5 - Realizar multiplicação com numeros binarios')
    print('6 - Realizar divisão com numeros binarios')
    print('7 - Registrar números decimais')
    print('8 - Voltar ao menu principal')
    print("=" * 45)


def menu_matriz_loop():
    matrizes = {}
    while True:
        menu_MATRIZ()
        try:
            opcao = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Entrada inválida. Digite um número.\n")
            continue

        if opcao == 1:
            matrizes = criar_matriz()
        elif opcao in [2, 3, 4, 5, 6, 7]:
            if not matrizes:
                print("Erro: Nenhuma matriz foi criada ainda.\n")
                continue
            operar_matrizes(matrizes, op=opcao)
        elif opcao == 8:
            print("Voltando ao menu principal...\n")
            break
        else:
            print("Opção inválida. Tente novamente.\n")
        
        


def menu_binario_loop(): #LOOP DO MENU, ENQUANTO O NUMERO DE ENTRADA FOR DIFERENTES DE 5, O LOOP CONTINUA
    while True:
        menu_BINARIO()
        try:
            opcao = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Entrada inválida. Digite um número.\n")
            continue
    
        match opcao:



            case 1:
                num_dec = (input("Digite um numero decimal:"))
                converter_binario(num_dec)
                num_dec = (input("Digite um numero decimal:"))
                converter_binario(num_dec)
            case 2:
                num_bin = (input("Digite um numero binario:"))
                converter_decimal(num_bin)
                num_bin = (input("Digite um numero binario:"))
                converter_decimal(num_bin)
            case 3:
                num1_bin = (input("Digite o primeiro numero binario:"))
                num2_bin = (input("Digite o segundo numero binario:"))
                soma_binario(num1_bin, num2_bin)
                num1_bin = (input("Digite o primeiro numero binario:"))
                num2_bin = (input("Digite o segundo numero binario:"))
                soma_binario(num1_bin, num2_bin)
            case 4:
                num1_bin = (input("Digite o primeiro numero binario:"))
                num2_bin = (input("Digite o segundo numero binario:"))
                subtrair_binario(num1_bin, num2_bin)
                num1_bin = (input("Digite o primeiro numero binario:"))
                num2_bin = (input("Digite o segundo numero binario:"))
                subtrair_binario(num1_bin, num2_bin)
            case 5:
                num1_bin = (input("Digite o primeiro numero binario:"))
                num2_bin = (input("Digite o segundo numero binario:"))
                multiplicar_binario(num1_bin,num2_bin)
            case 6:
                num1_bin = (input("Digite o primeiro numero binario:"))
                num2_bin = (input("Digite o segundo numero binario:"))
                dividir_binario(num1_bin,num2_bin)
            case 7:
                registrar_numero()
            case 8:
                print("Encerrando o programa. Até logo!")
                break
            case _:
                print('opção invalida')


def main():
    print("\nBem-vindo à Calculadora Geral!")

    while True:
        menu_principal()
        try:
            escolha = int(input("\nDigite a opção desejada: "))
        except ValueError:
            print("Entrada inválida. Digite um número.\n")
            continue

        if escolha == 1:
            menu_binario_loop()
        elif escolha == 2:
            menu_matriz_loop()
        elif escolha == 3:
            print("Encerrando o programa. Até logo!")
            break
        else:
            print("Opção inválida. Tente novamente.\n")

main()
