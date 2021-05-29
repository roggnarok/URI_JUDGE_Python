# 1079 - Médias Ponderadas
n = int(input())
for i in range(n):
    valores = [float(x) for x in input().split()]
    a = valores[0]
    b = valores[1] 
    c = valores[2]
    media = ((a*2)+(b*3)+(c*5))/10
    print(f'{media:.1f}')