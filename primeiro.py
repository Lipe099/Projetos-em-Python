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
