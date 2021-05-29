# URI 1049 - ANIMAL 
''' Ler 3 palavras que definem o tipo de aninal possível segundo o 
esquema abaixo, da esquerda para a direita. Em seguida conclua
qual dos anumais seguintes foi escolhido.'''
# Recebe as entradas do usuário e converte para minúscula. 
t1 = input().lower()
t2 = input().lower()
t3 = input().lower()

# Define as veriváveis
ver = 'vertebrado'
ave = 'ave'
mam = 'mamifero'
car = 'carnivoro'
oni = 'onivoro'
her = 'herbivoro'
inv = 'invertebrado'
ins = 'inseto'
ane = 'anelideo'
hem = 'hematofago'

# Define a tupla com os animais
aguia = (ver, ave, car)
pomba = (ver, ave, oni)
homem = (ver, mam, oni)
vaca = (ver, mam, her )
pulga = (inv, ins, hem)
lagarta = (inv, ins, her)
sanguessuga = (inv, ane, hem)
minhoca = (inv, ane, oni)

# Faz as verificações. 
if t1 in aguia and t2 in aguia and t3 in aguia:
    print("aguia")
if t1 in pomba and t2 in pomba and t3 in pomba:
    print("pomba")
if t1 in homem and t2 in homem and t3 in homem:
    print("homem")
if t1 in vaca and t2 in vaca and t3 in vaca:
    print("vaca")
if t1 in pulga and t2 in pulga and t3 in pulga:
    print("pulga")
if t1 in lagarta and t2 in lagarta and t3 in lagarta:
    print("lagarta")
if t1 in sanguessuga and t2 in sanguessuga and t3 in sanguessuga:
    print("sanguessuga")
if t1 in minhoca and t2 in minhoca and t3 in minhoca:
    print("minhoca")