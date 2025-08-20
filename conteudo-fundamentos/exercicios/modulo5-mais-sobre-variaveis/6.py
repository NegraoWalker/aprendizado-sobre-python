# 6. Faça um programa que calcule a área de uma sala de um apartamento. Para isso, o seu programa precisa pedir a largura da sala, o comprimento da sala e imprimir a área em m^2 da sala.
largura_sala_str = input("Informe a largura da sala: ")
comprimento_sala_str = input("Informe o comprimento da sala: ")

area_sala = float(largura_sala_str) * float(comprimento_sala_str)

print(f"Área da sala: {area_sala}")