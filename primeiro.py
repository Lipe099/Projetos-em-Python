def registrar_numero():
   regis_num={}
def converter_binario(num):
    numero = float(num)
    int_num = int(numero)
    fra_num = numero - int_num

    if fra_num != 0:
      
     
      int_bin = bin(int_num)[2:]
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
       res = bin(int(numero))[2:]
       print(f" o numero binario do numero decimal{numero} é {res}")

    return res
    

def converter_decimal(num):

    num_binario = num
    

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
    return decimal

def soma_binario(pri_binario,seg_binario):


 r = converter_decimal(pri_binario) 
 l = converter_decimal(seg_binario)
 k = r +l 

 res_bin = converter_binario(k)


 print(f"O resultado é {res_bin}")

 
 