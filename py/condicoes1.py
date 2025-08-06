salario = float (input("Informe o salário:"))

if salario <= 3000:
    print("salario inicial")
elif salario >3000 and salario <=6000:
    print("salario médio")
elif salario >6000 and salario <=15000:
    print("salario superior")
else:
    print("salario gerente")