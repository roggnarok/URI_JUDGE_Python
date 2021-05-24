'''
                    MÉDIA 1
    Leia 2 valores de ponto flutuante A e B.
    A seguir, calcule a média do aluno, sabendo que
    a nota A tem peso 3.5 e a nota B tem peso 7.5. 
'''
def media(a, b):
    m = ((a * 3.5) + (b * 7.5)) / 11
    return m


# Programa Principal.
x = float(input())
y = float(input())
print(f'MEDIA = {media(x, y):.5f}')