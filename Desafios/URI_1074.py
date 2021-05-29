n1 = int(input())
while n1 > 10000:
    n1 = int(input())
for i in range(n1):
    x = int(input())
    if x < 0:
        if (x % 2) == 0:
            print('EVEN NEGATIVE')
        else:
            print('ODD NEGATIVE')
    if x == 0:
        print('NULL')
    if x > 0:
        if (x % 2) == 0:
            print('EVEN POSITIVE')
        else:
            print('ODD POSITIVE')