'''
                                     SOMA SIMPLES
Leia dois valores inteiros, no caso para variáveis A e B.
A seguir, calcule a soma entre elas e atribua à variável SOMA.
Imprima a mensagem "SOMA" com todas as letras maiúsculas,
com um espaço em branco antes e depois da igualdade seguido pelo
valor correspondente à soma de A e B.
'''
def soma(a, b):          # Define uma função chamada soma, que recebe dois valores a,b.
    s = a + b               # Realiza a soma dos valores
    return s                # Retorna o resultado


#Programa principal.
a = int(input())          # Lê do usuário um valor, converte p/ inteiro e atribui a variável a.
b = int(input())          # Lê do usuário um valor, converte p/ inteiro e atribui a variável b.
print(f'SOMA = {soma(a,b)}')    # Imprime na tela o resultado. 