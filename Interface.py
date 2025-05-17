from primeiro import converter_binario, converter_decimal, soma_binario


print("="*40)
print('converte um numero decimal para binario --- (1)')
print('converte um numero binario para decimal --- (2)')
print('Realizar soma com numeros binarios -------- (3)')
print('Realizar subtração com numeros binarios --- (4)')
print("="*40)
opcao = int(input('\nqual e a opção desejada?:'))

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
    # case 4:

    case _:
        print('opção invalida')


