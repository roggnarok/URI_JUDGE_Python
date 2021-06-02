#1013 - O maior número entre 3
linha = input() .split()
a = int(linha[0])
b = int(linha[1])
c = int(linha[2])
maiorab = ((a+b+abs(a-b)))/2
maiorABouC = ((maiorab+c+abs(maiorab-c)))/2
print("%i eh o maior"%maiorABouC)