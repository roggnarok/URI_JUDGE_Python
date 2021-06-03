#1015 - Distância entre dois pontos
ponto1 = input() .split()
x0 = float(ponto1[0])
y0 = float(ponto1[1])
ponto2 = input() .split()
x1 = float(ponto2[0])
y1 = float(ponto2[1])

dist = ((((x1-x0)**2)+((y1-y0)**2))**(1/2))
print("%.4f"%dist)