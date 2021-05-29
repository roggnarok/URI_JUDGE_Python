# 1075 - RESTO 2
'''Leia um valor inteiro N.
Apresente todos os números entre 1 e 10000
    que divididos por N dão resto igual a 2.'''

n1 = int(input())
while n1 > 10000:
    n1 = int(input())
for i in range(1,10001):
    if (i % n1) == 2:
        print(i)