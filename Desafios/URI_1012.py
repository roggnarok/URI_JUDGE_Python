#1012 - Área de várias geometrias com input de 3 variáveis.
linha = input() .split()
a = float(linha[0])
b = float(linha[1])
c = float(linha[2])

PI=3.14159
a_trian = (a*c)/2
a_circ = PI*(c**2)
a_trap = ((a+b)*c)/2
a_quad = b*b
a_reta = a*b
print(
f'TRIANGULO: {a_trian:.3f}\n'
'CIRCULO: {a_circ:.3f}\nTRAPEZIO: {a_trap:.3f}\n'
'QUADRADO: {a_quad:.3f}\nRETANGULO: {a_reta:.3f}'
)