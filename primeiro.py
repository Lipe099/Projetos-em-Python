def registrar_numero():
   regis_num={}
def converter_binario(num):
    numero = float(num)
    int_num = int(numero)
    fra_num = numero - int_num

    if fra_num != 0:
      
      int_bin = bin(int_num)[2:]
      fra_bin = ""
      
      while fra_num and len(fra_bin) < 10:
         fra_num *= 2
         bit = int(fra_num)
         fra_bin += str(bit)
         fra_num -= bit
        
      num_bin = int_bin + "." + fra_bin  

      print(f"O numero decimal {numero} fica {num_bin} em binario")

    else: 
       numero = int(numero)
       num_bin = bin(numero)[2:]
       print(f"O numero decimal {numero} fica {num_bin} em binario")

    return num_bin
    
def converter_decimal(num):

    num_binario = num
    
    if '.' in num_binario:
        parte_inteira, parte_fracionaria = num_binario.split('.')

        decimal = int(parte_inteira, 2)

        for i,  bit in enumerate(parte_fracionaria):
            if bit == '1':
                decimal += 1/2**(i+1)
        print(f"O numero binario {num_binario} em decimal fica {decimal} ")
    else:
        decimal = int(num_binario, 2)
        print(f"o numero decimal do numero binario {num_binario} é {decimal}")
    return decimal

def soma_binario(pri_binario,seg_binario):

 pri_dec = converter_decimal(pri_binario) 
 seg_dec = converter_decimal(seg_binario)
 res = pri_dec + seg_dec 

 res_bin = converter_binario(res)

 print(f"O resultado da soma é {res_bin}")

def subtrair_binario(pri_binario,seg_binario):
 
 pri_dec = converter_decimal(pri_binario) 
 seg_dec = converter_decimal(seg_binario)
 res = pri_dec - seg_dec 

 res_bin = converter_binario(res)
  

 print(f"O resultado é {res_bin}")

def multiplicar_binario(pri_binario,seg_binario):
 
 pri_dec = converter_decimal(pri_binario)
 seg_dec = converter_decimal(seg_binario)
 res = pri_dec * seg_dec

 res_bin = converter_binario(res)

 print(f" O resultado em decimal é {res} e em binario é {res_bin} ")

def dividir_binario(pri_binario,seg_binario):
  
 pri_dec = converter_decimal(pri_binario)
 seg_dec = converter_decimal(seg_binario)
 res = pri_dec / seg_dec

 res_bin = converter_binario(res)

 print(f" O resultado em decimal é {res} e em binario é {res_bin} ")

  
 