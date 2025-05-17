def converter_binario():
    numero = (input("digite o numero decimal: "))

    if '.' in numero:
      antes, depois = numero.split('.')
      fra_num = float("0."+ depois)
      int_num = int(antes)
     
      int_bin = bin(int(int_num))[2:]
      fra_bin = ""
      print(f" {fra_num}")

      while fra_num and len(fra_bin) < 10:
         fra_num *= 2
         bit = int(fra_num)
         fra_bin += str(bit)
         fra_num -= bit
        
      res = int_bin + "." + fra_bin  

        

      print(f" o numero binario do decimal {numero} é {res} |")

    
    else: 
       binario = bin(int(numero))[2:]
       print(f" o numero binario do numero decimal{numero} é {binario}")
    

def converter_decimal(num_bin):

    num_binario = int(num_bin)

    if '.' in num_binario:
        parte_inteira, parte_fracionaria = num_binario.split('.')

        decimal = int(parte_inteira, 2)

        for i,  bit in enumerate(parte_fracionaria):
            if bit == '1':
                decimal += 1/2**(i+1)

        print(f"o numero decima do binario {num_binario} é {decimal} ")

    else:

        decimal = int(num_binario, 2)

        print(f"o numero decimal do numero binario {num_binario} é {decimal}")
    return

def soma_binario():

 pri_binario = int(input("Digite o primeiro numero binario:") )  
 seg_binario = int(input("Digite o segundo numero binario:") )

 pri_dec = converter_decimal(pri_binario)
 seg_dec = converter_decimal(seg_binario)

 res = pri_dec+ seg_dec

 res_bin = converter_binario(res)

 print(f"O resultado é {res_bin}")

 
 