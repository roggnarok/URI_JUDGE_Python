#1009 - Ler o Nome, Salário, Valor das vendas, informar o valor a receber no final do mês
nome=input()
salario=float(input())
vendas=float(input())
montante=(salario+(0.15*vendas)) #Comissão equivale a 15% do total vendido.
print("TOTAL = R$ %.2f"%montante)