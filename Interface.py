from primeiro import converter_binario, converter_decimal, soma_binario, subtrair_binario


print("="*40)
print('converte um numero decimal para binario --- (1)')
print('converte um numero binario para decimal --- (2)')
print('Realizar soma com numeros binarios -------- (3)')
print('Realizar subtração com numeros binarios --- (4)')
print("="*40)
opcao = int(input('\nqual e a opção desejada?:'))

match opcao:

    case 1:
        converter_binario()
    case 2:
        converter_decimal()
 
    case 3:
        soma_binario()

    case 4:
        subtrair_binario
    
    case _:
        print('opção invalida')












