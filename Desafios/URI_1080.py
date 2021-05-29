#1080 - Maior e Posição
# Cria uma lista vazia []
list = []
# Recebe os 100 valores do usuário.
for i in range(100):
    list.append(int(input()))
# Maior valor da lista.
print(max(list))
# Posição do maior valor da lista. Posição =  index + 1.
print((list.index(max(list)))+1)