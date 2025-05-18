from primeiro import converter_binario, converter_decimal, soma_binario, subtrair_binario, multiplicar_binario,dividir_binario

def menu():
    print("=" * 45)
    print(f"|===={'CALCULADORA DE BINÁRIOS':^35}====|")
    print("=" * 45)
    print('converte um numero decimal para binario--- (1)')
    print('converte um numero binario para decimal--- (2)')
    print('Realizar soma com numeros binarios-------- (3)')
    print('Realizar subtração com numeros binarios--- (4)')
    print('Realizar multiplicação com numeros binarios(5)')
    print('Realizar divisão com numeros binarios------(6)')
    print("Sair-------------------------------------- (7)")
    print("="* 45)

def main():
   
    while True:
        menu()  # mosta ao usuario as opcoes disponiveis
        opcao = int(input("\nDigite a opção desejada:"))
        print("")
        
        match opcao:
            
            case 1:
                num_dec = (input("Digite um numero decimal:"))
                converter_binario(num_dec)
            case 2:
                num_bin = (input("Digite um numero binario:"))
                converter_decimal(num_bin)
            case 3:
                num1_bin = (input("Digite o primeiro numero binario:"))
                num2_bin = (input("Digite o segundo numero binario:"))
                soma_binario(num1_bin, num2_bin)
            case 4:
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
                print('encerrando o programa. Até logo')
                break
            
            case _:
                print('opção invalida')



main()
