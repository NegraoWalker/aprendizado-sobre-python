# ==================================================
#  Exemplos de Operadores Aritméticos em Python
# ==================================================

# 1.1. Soma e Subtração: calcular gastos e receber troco
preco_almoco = 25.50
valor_pago = 50.00

troco = valor_pago - preco_almoco   # Subtração
print(f"Você deu R${valor_pago:.2f} e o almoço custou R${preco_almoco:.2f}. Seu troco é R${troco:.2f}.")

# 1.2. Multiplicação: calcular total da compra
preco_maçã = 3.20
quantidade_maçã = 4

total_maçãs = preco_maçã * quantidade_maçã   # Multiplicação
print(f"Cada maçã custa R${preco_maçã:.2f}. Você comprou {quantidade_maçã}. Total: R${total_maçãs:.2f}.")

# 1.3. Divisão real vs. Divisão inteira: dividir lanches entre amigos
total_lanches = 10
amigos = 3

por_amigo_real = total_lanches / amigos     # Divisão que retorna float
por_amigo_inteiro = total_lanches // amigos # Divisão inteira (parte inteira)
resto_lanches = total_lanches % amigos      # Módulo (resto)
print(f"Divisão real: {total_lanches}/{amigos} = {por_amigo_real:.2f} lanches por amigo.")
print(f"Divisão inteira: {total_lanches}//{amigos} = {por_amigo_inteiro} lanches inteiros por amigo, sobram {resto_lanches} lanches.")

# 1.4. Módulo para checar par ou ímpar
numero = 17
if numero % 2 == 0:   # Resto da divisão por 2 igual a zero ⇒ número par
    print(f"{numero} é par.")
else:
    print(f"{numero} é ímpar.")

# 1.5. Exponenciação: calcular potência de base e expoente
base = 5
expoente = 3
resultado_potencia = base ** expoente
print(f"{base} elevado à potência {expoente} é {resultado_potencia}.")

# 1.6. Operadores unários (+ e -)
valor = 10
print(f"Negação de {valor} é {-valor}.")
print(f"O operador + em +{valor} deixa o valor como está (simplesmente {+valor}).")
