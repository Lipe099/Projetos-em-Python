numero = int(input("digite o numero decimal: "))
saida = []

if numero % 2:

 while numero > 0:
  saida.append(numero%2)
  numero //=2

 saida.reverse()
 print( f" O numero em binario será: {saida}")
