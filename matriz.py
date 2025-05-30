import numpy as np

def criar_matriz():  # permite o usuário criar matrizes
    matrizes = {}  # Dicionário para armazenar as matrizes com nomes
    # usuario informa o numero de matrizes que ele deseja criar
    quantidade = int(input("quantas matrizes você deseja criar:"))

    for i in range(quantidade):
        nome = input(f"Digite o nome da matriz {i+1}:") # O usuário informa o nome da matriz.
        linhas = int(input(f"Digite o número de linhas da {nome}: ")) # O usuário informa a ordem da matriz.
        colunas = int(input(f"Digite o número de colunas da {nome}: ")) # O usuário informa a ordem da matriz.

        # O usuário passa os valores da matriz da ordem especificada por ele.
        print(f"Digite os valores da matriz {nome} ({linhas}x{colunas}):")
        matriz = np.empty((linhas, colunas), dtype=int) # cria uma matriz vazia. OBS:dtype define os tipos de dados(inteiros)

        for l in range(linhas):  # usamos range para gerar um intervalo, mas estamos usando (linhas) para informar a quantidade da sequencia
            for c in range(colunas):  # mesma coisa, soq para coluna.
                # O codigo pede o valor, informando a posição correspondente. ex matriz 2x2: (0.0),(0.1),(1.0),(1.1)
                valor = int(input(f"Valor para a posição [{l}][{c}]: "))
                matriz[l][c] = valor
                matrizes[nome] = matriz  # Armazena a matriz no dicionário
        print(f"Matriz {nome} criada:\n{matriz}")
    return matrizes  # Retorna a matriz


def operar_matrizes(matrizes, op):
    # Operações que exigem duas matrizes (soma, subtração, multiplicação)
    if op in [2, 3, 4]:
        matrizA_nome = input(
            "Digite o nome da primeira matriz para a operação: ")
        matrizB_nome = input(
            "Digite o nome da segunda matriz para a operação: ")

        # acessa o dicionario "matrizes" e "verifica" se a matriz existe no dicionaro, caso nao exista get retorna "none/vazio"
        matrizA = matrizes.get(matrizA_nome)
        matrizB = matrizes.get(matrizB_nome)

        if matrizA is None or matrizB is None:
            print("Erro: Uma ou ambas as matrizes não existem.")
            return

        if matrizA.shape != matrizB.shape and op != 4:
            print(
                "Erro: As matrizes devem ter o mesmo formato para realizar esta operação.")
            return

        if op == 2:
            resultado = matrizA + matrizB
        elif op == 3:
            resultado = matrizA - matrizB
        elif op == 4:
            if matrizA.shape[1] != matrizB.shape[0]:
                print("Erro: Para a multiplicação matricial, o número de colunas da primeira matriz deve ser igual ao número de linhas da segunda matriz.")
                return
            resultado = matrizA @ matrizB  # Multiplicação matricial
    elif op == 5:# Cálculo da determinante da matriz
            matrizA_nome = input(
                "Digite o nome da matriz para a operação:")

            matrizA = matrizes.get(matrizA_nome)

            if matrizA is None:
                print(" matriz não exite!! ")
                return

            det_matrizA = np.linalg.det(matrizA) #determinante da matriz
            
            if 0 < det_matrizA < 2:
                det_matrizA = 1


            print(int(det_matrizA))

            print('ola estou em desnvolvimento')
            return
    elif op == 6:# Cálculo da matriz inversa
            matrizA_nome = input(
                "Digite o nome da matriz para a operação:")

            matrizA = matrizes.get(matrizA_nome)

            if matrizA is None:
                 print(" matriz não exite!! ")
                 return

            inv_matrizA = np.linalg.inv(matrizA) #matriz inversa
            
            print(inv_matrizA)

            
            return

    elif op == 7:  # Cálculo da transposta
        # mesmo esquema, matrizA quando o nome acessa o nome no dicionario
        matrizA_nome = input(
            "Digite o nome da matriz para calcular a transposta: ")
        matrizA = matrizes.get(matrizA_nome)

        if matrizA is None:
            print("Erro: A matriz selecionada não existe.")
            return

        resultado = matrizA.T  # Transposta da matriz
        
    elif op == 8:  
        matrizA_nome = input("Digite o nome da Matriz: ")

        matrizA = matrizes.get(matrizA_nome) 

        maior = menor = matrizA[1][0]

        for linha in matrizA:
          for valor in linha:
            if valor > maior:
               maior = valor
            if valor < menor:
               menor = valor

        print(f"{maior} é o maior numero da matriz, {menor} é o menor numero da matriz")
        return
    
    elif op == 9:
        matrizA_nome = input("Digite o nome da primeira matriz:")
        matrizB_nome = input("Digite o nome da segunda matriz:")
        matrizC_nome = input("Digite o nome da terceira matriz:")

        matrizA = matrizes.get(matrizA_nome)
        matrizB = matrizes.get(matrizB_nome)
        matrizC = matrizes.get(matrizC_nome)

        opção = input("Qual sera a operação?:")

        if opção == 'a' or 'A':
           resposta = matrizA.T - 2*matrizB + np.linalg.inv(matrizC)
        elif opção == 'b' or 'B':
           resposta = matrizB.T - matrizA*matrizC
        else:
            print("opção invalida")
        
        print(f" o resultado é {resposta}")

        return

    else:
        print("Operação inválida.")
        return

    print(f"Resultado da operação {op}:")
    print(resultado)