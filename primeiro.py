

def converter_binario(num):
    numero = float(num)
    int_num = int(numero)
    fra_num = numero - int_num

    if fra_num != 0:

        int_bin = bin(int_num)[2:]
      
        int_bin = bin(int_num)[2:]
        fra_bin = ""
        print(f" {fra_num}")

        while fra_num and len(fra_bin) < 10:
            fra_num *= 2
            bit = int(fra_num)
            fra_bin += str(bit)
            fra_num -= bit
        num_bin = int_bin + "." + fra_bin  

    else: 
       numero = int(numero)
       num_bin = bin(numero)[2:]
       
    return num_bin
   
def converter_decimal(num):
    num_binario = num

    if '.' in num_binario:
        parte_inteira, parte_fracionaria = num_binario.split('.')

        decimal = int(parte_inteira, 2)

        for i,  bit in enumerate(parte_fracionaria):
            if bit == '1':
                decimal += 1/2**(i+1)
       
    else:
        decimal = int(num_binario, 2)
       
    return decimal
 
def soma_binario():
  
  bin1 = input('Digite o primeiro numero binario:')
  bin2 = input("Digite o segundo numero binario:")

    
  if '.' in bin1:
        int1, frac1 = bin1.split('.')
  else:
        int1, frac1 = bin1, '' 
        
  if '.' in bin2:
        int2, frac2 = bin2.split('.')
  else:
        int2, frac2 = bin2, '' 

  max_frac_len =max(len(frac1), len(frac2))
  frac1 = frac1.ljust(max_frac_len, '0')
  frac2 = frac2.ljust(max_frac_len, '0')

  max_int_len = max(len(int1),len(int2))
  int1 = int1.zfill(max_int_len)
  int2 = int2.zfill(max_int_len)

  resultado_int = ''  
  resultado_frac = ''
  carry = 0
  for i in range(max_frac_len -1,-1,-1):
        bit1 = int(frac1[i])
        bit2 = int(frac2[i])
        total = bit1 + bit2 + carry
        resultado_frac = str(total % 2) + resultado_frac
        carry = total // 2

  
  for i in range(max_int_len-1,-1,-1):
        bit1 = int(int1[i])
        bit2 = int(int2[i])
        total = bit1 + bit2 + carry
        resultado_int = str(total %2 ) + resultado_int
        carry = total//2

  
  if carry:
         resultado_int = '1' + resultado_int 

  soma_final = resultado_int + '.' + resultado_frac
  
  print(f" o resultado é {soma_final} e seu valor em decimal  é {converter_decimal(soma_final)}")
     


def subtrair_binario():
  
  bin1 = input('Digite o primeiro numero binario:')
  bin2 = input("Digite o segundo numero binario:")

    
  if '.' in bin1:
        int1, frac1 = bin1.split('.')
  else:
        int1, frac1 = bin1, '' 
        
  if '.' in bin2:
        int2, frac2 = bin2.split('.')
  else:
        int2, frac2 = bin2, '' 

  max_frac_len =max(len(frac1), len(frac2))
  frac1 = frac1.ljust(max_frac_len, '0')
  frac2 = frac2.ljust(max_frac_len, '0')

  max_int_len = max(len(int1),len(int2))
  int1 = int1.zfill(max_int_len)
  int2 = int2.zfill(max_int_len)

  negativo = False
  if bin1 < bin2:
       int1, int2 = int2, int1
       frac1, frac2 = frac2 ,frac1
       negativo = True

  resultado_int = ''  
  resultado_frac = ''
  borrow = 0
  for i in range(max_frac_len -1,-1,-1):
        bit1 = int(frac1[i]) - borrow
        bit2 = int(frac2[i])
        if bit1 < bit2:
            bit1 += 2
            borrow = 1
        else:
             borrow = 0
        resultado_frac = str(bit1 - bit2) + resultado_frac
        

  for i in range(max_int_len-1,-1,-1):
        bit1 = int(int1[i]) - borrow
        bit2 = int(int2[i])
        if bit1 < bit2:
            bit1 += 2
            borrow = 1
        else:
             borrow = 0
        resultado_int = str(bit1 - bit2) + resultado_int

  resultado_int = resultado_int.lstrip('0')# retira os zeros que foram adicionados à esquerda
  resultado_frac = resultado_frac.rstrip('0')# retira os zero que foram adicionados à direita
  
  if negativo == True:
    soma_final = '-' + resultado_int + '.' + resultado_frac
  else:
   soma_final = resultado_int + '.' + resultado_frac
  
  print(f" o resultado é {soma_final} e seu valor em decimal  é {converter_decimal(soma_final)}")


  
 
