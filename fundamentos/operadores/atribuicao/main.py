# ==============================================================
#  Exemplos de Operadores de Atribuição (combinados com aritmética)
# ==============================================================

# 2.1. Atribuição simples
x = 10
print(f"Inicialmente, x = {x}")

# 2.2. Incrementar com +=
x += 5       # equivale a x = x + 5
print(f"Depois de x += 5, x = {x}")  # x agora vale 15

# 2.3. Decrementar com -=
x -= 3       # equivale a x = x - 3
print(f"Depois de x -= 3, x = {x}")  # x agora vale 12

# 2.4. Multiplicar com *=
x *= 2       # equivale a x = x * 2
print(f"Depois de x *= 2, x = {x}")  # x agora vale 24

# 2.5. Dividir com /= (resulta em float)
x /= 4       # equivale a x = x / 4
print(f"Depois de x /= 4, x = {x}")  # x agora vale 6.0

# 2.6. Divisão inteira com //=
x //= 2      # equivale a x = x // 2 (parte inteira)
print(f"Depois de x //= 2, x = {x}")  # x agora vale 3.0 (pois 6.0 // 2 = 3.0)

# 2.7. Resto da divisão com %=
x %= 2       # equivale a x = x % 2
print(f"Depois de x %= 2, x = {x}")  # x agora vale 1.0 (resto de 3.0/2 = 1.0)

# 2.8. Exponenciação composta com **=
y = 2
y **= 5      # equivale a y = y ** 5
print(f"Depois de y **= 5, y = {y}")  # y agora vale 32 (2^5)

# 2.9. Exemplo real: calcular saldo de conta com juros mensais consecutivos
saldo = 1000.0
juros_mensal = 0.01  # 1% ao mês

# Aplicar juros 3 meses seguidos
for mes in range(1, 4):
    saldo *= (1 + juros_mensal)  # cada mês: saldo = saldo * 1.01
    print(f"Mês {mes}: Saldo com juros = R${saldo:.2f}")
