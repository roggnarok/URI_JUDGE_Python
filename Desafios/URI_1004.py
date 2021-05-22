'''
                            PRODUTO SIMPLES
Leia dois valores inteiros A e B. Calcule o produto entre
estes dois valores e atribua esta operação à variável PROD.
A seguir mostre a variável PROD com mensagem correspondente.
'''
def multiplicar(a, b):      # Define uma função chamada MULTIPLICAR, que recebe dois valores a,b.
    return (a * b)              # Realiza o produto dos valores recebidos e Retorna o resultado.


#Programa principal.
a=int(input())              # Lê do usuário um valor, converte p/ inteiro e atribui a variável a.
b=int(input())              # Lê do usuário um valor, converte p/ inteiro e atribui a variável b.
PROD = multiplicar(a,b)     # A variável PROD recebe o retorno da função multiplicar. 
print(f'PROD = {PROD}')     # Imprime na tela o resultado. 