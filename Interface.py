from primeiro import converter_binario, converter_decimal, soma_binario

def menu():
   print("="*40)
   print('converte um numero decimal para binario --- (1)')
   print('converte um numero binario para decimal --- (2)')
   print('Realizar soma com numeros binarios -------- (3)')
   print('Realizar subtração com numeros binarios --- (4)')
   print("Sair-------(5)")
   print("="*40)

def main():
    print("\nBem-vindo à Calculadora de numeros binários!")  # Apresenta o programa

    while True:
        menu()  # mosta ao usuario as opcoes disponiveis
        opcao = int(input("\nDigite a opção desejada:"))
        print("")
        match opcao:

            case 1:
                converter_binario()
            case 2:
                converter_decimal()
        
            case 3:
                soma_binario()

            #case 4:
            case 5:
                return(menu)
            
            case _:
                print('opção invalida')

main()
   













