# 1078 - Tabuada
n = int(input())
while n < 2 or n > 1000:
    n = int(input())
for i in range(1,11):
    print(f'{i} x {n} = {i*n}')