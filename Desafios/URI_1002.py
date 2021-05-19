'''
                                Área do Círculo.
    Entrada contém um valor de ponto flutuante (dupla precisão), a variável raio.
    Saída apresentar a mensagem "A=" seguido pelo valor da variável area,
        c/ 4 casas após o ponto decimal.
'''
from math import pi             # Importa a constante pi da biblioteca math.


def area(raio: float):          # Define uma função chamada area que recebe um float.
    return (pi * (raio **2))        # Retorna o valor da área que foi calculada.


raio = float(input())           # Recebe do usuário o valor do raio.
resultado = area(raio)          # Armazena na variável resultado o retorno da função area.
print(f'A={resultado:.4f}')     # Exibe na tela o resultado da área nos padrões exigidos pelo desafio!