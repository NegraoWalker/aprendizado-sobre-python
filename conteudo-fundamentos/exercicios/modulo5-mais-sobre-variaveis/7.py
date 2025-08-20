# 7. Faça um programa que pergunte quanto você ganha por hora e o número de horas trabalhadas no mês. Calcule e mostre o total do seu salário no referido mês.
valor_por_hora_str = input("Informe o valor por hora: ")
numero_de_horas_trabalhadas = input("Informe o número de horas trabalhadas: ")

salario = float(valor_por_hora_str) * float(numero_de_horas_trabalhadas)

print(f"Salário: R${salario}")