def media(a, b):
    m = ((a * 3.5) + (b * 7.5))/ 11
    return m


# Programa Principal.
x = float(input())
y = float(input())
print(f'MEDIA = {media(x, y):.5f}')