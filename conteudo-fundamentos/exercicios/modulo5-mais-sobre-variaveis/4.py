# 4. Faça um programa que peça as 4 notas bimestrais de um aluno e mostre a média de todas as notas
nota_1_str = input("Informe a primeira nota: ")
nota_2_str = input("Informe a segunda nota: ")
nota_3_str = input("Informe a terceira nota: ")
nota_4_str = input("Informe a quarta nota: ")

media = (float(nota_1_str) + float(nota_2_str) + float(nota_3_str) + float(nota_4_str)) / 4

print(f"A média das notas foi: {media}")