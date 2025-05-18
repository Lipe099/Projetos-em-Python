import decimal


def registrar_numero():
   regis_num={}
   quantidade= int(input('quantidade de numeros que deseja registrar: '))
  
   for i in range(quantidade):
      nome = input(f'Nome para o número {i + 1}: ')
      valor= int(input('\nDigite o numero: '))
      try:
         numero=converter_binario(valor)
         regis_num[nome]=valor
         print(f"\nRegistrado: {nome} = {valor} -> binário: {numero}\n")

      except:
        print('Entrada inválida! Certifique-se de digitar um número.\n')

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
      num_bin = int_bin + "." + fra_bin  

      print(f" o numero binario do decimal {numero} é {res} |")
      print(f"O numero decimal {numero} fica {num_bin} em binario")

    else: 
       numero = int(numero)
       res = bin(numero)[2:]
       print(f" o numero binario do numero decimal{numero} é {res}")
       num_bin = bin(numero)[2:]
       print(f"O numero decimal {numero} fica {num_bin} em binario")

    return res,num_bin
   
def converter_decimal(num):

    num_binario = num
    
    num_binario = num
    
    if '.' in num_binario:
        parte_inteira, parte_fracionaria = num_binario.split('.')

        decimal = int(parte_inteira, 2)

        for i,  bit in enumerate(parte_fracionaria):
            if bit == '1':
                decimal += 1/2**(i+1)
        print(f"O numero binario {num_binario} em decimal fica {decimal} ")
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

def subtrair_binario(pri_binario,seg_binario):#observação: realisar um filtro pra resultados negativos
 
 pri_dec = converter_decimal(pri_binario) 
 seg_dec = converter_decimal(seg_binario)
 res = pri_dec - seg_dec 

 res_bin = converter_binario(res)
  
 print(f"O resultado da subtração é {res_bin}")

def multiplicar_binario(pri_binario,seg_binario):
 
 pri_dec = converter_decimal(pri_binario)
 seg_dec = converter_decimal(seg_binario)
 res = pri_dec * seg_dec

 res_bin = converter_binario(res)

 print(f"O resultado da multipliacação é {res_bin} ")

def dividir_binario(pri_binario,seg_binario):
  
 pri_dec = converter_decimal(pri_binario)
 seg_dec = converter_decimal(seg_binario)
 res = pri_dec / seg_dec

 res_bin = converter_binario(res)

 print(f"O resultado da divisão é {res_bin} ")

  
 
