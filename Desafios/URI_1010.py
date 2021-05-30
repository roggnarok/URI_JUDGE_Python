#1010 - deve-se ler o código de uma peça 1, o número de peças 1, o valor unitário de cada peça. Após, calcule e mostre o valor a ser pago.
linha = input() .split()
c1 = int(linha[0])
n1 = int(linha[1])
v1 = float(linha[2])

linha1 = input() .split()
c2 = int(linha1[0])
n2 = int(linha1[1])
v2 = float(linha1[2])

valorpago = ((n1*v1)+(n2*v2))
print("VALOR A PAGAR: R$ %.2f"%valorpago)