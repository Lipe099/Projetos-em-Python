from primeiro import converter_binario, converter_decimal

 
print(' opcoes')
print('converte um numero decimal para binario --- (1)')
print('converte um numero binario para decimal --- (2)')
print('Realizar soma com numeros binarios --- (3)')
print('Realizar subtração com numeros binarios --- (4)')
opcao = int(input('\nqual e a opção desejada?:'))

match opcao:

    case 1:
        converter_binario()
    case 2:
        converter_decimal()
 
    #case 3:

    #case 4:
     
    case _:
        print('opção invalida')












