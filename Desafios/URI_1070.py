'''
                            SEIS NÚMEROS ÍMPARES
Leia um valor inteiro X. 
Apresente os 6 valores ímpares consecutivos a partir de X,
um valor por linha, inclusive o X ser for o caso.
'''
x = int(input())        # Lê do usuário um valor, converte p/ inteiro e atribui a variável x.
if (x % 2) == 0:        # Verifica se x é par:
    x += 1                  # Se x for par, soma-se 1 ao valor de x.
for i in range(0, 6):    # Realiza um loop 6 vezes.
    print(f'{x}')           # Mostra o valor de x.
    x += 2                  # Incrementa 2 ao valor de x.