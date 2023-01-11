# Solicitar o valor do salário
#Calcular aumento de 10% para salário maior que 1250
#Calcular aumento de 15% para salário menor ou igual a 1250

salario = float(input("Quanto você recebe de salário? "))

if salario > 1250:
    aumento1 = salario * 0.1
    print(f"Você receberá um aumento no valor de {aumento1}")
if salario <= 1250:
    aumento2 = salario * 0.15
    print(f"Você receberá um aumento no valor de {aumento2}")    