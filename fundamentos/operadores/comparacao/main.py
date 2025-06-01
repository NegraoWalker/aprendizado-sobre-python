# =====================================================
#  Exemplos de Operadores de Comparação em Python
# =====================================================

# 3.1. Igualdade e diferença
a = 7
b = 10
print(f"a == b? {a == b}")   # False, 7 não é igual a 10
print(f"a != b? {a != b}")   # True, 7 é diferente de 10

# 3.2. Maior, menor, maior ou igual, menor ou igual
print(f"a > b? {a > b}")     # False
print(f"a < b? {a < b}")     # True
print(f"a >= 7? {a >= 7}")   # True
print(f"b <= 5? {b <= 5}")   # False

# 3.3. Identidade de objetos (is e is not)
lista1 = [1, 2, 3]
lista2 = [1, 2, 3]
lista3 = lista1

print(f"lista1 == lista2? {lista1 == lista2}")   # True (conteúdo igual)
print(f"lista1 is lista2? {lista1 is lista2}")   # False (objetos diferentes)
print(f"lista1 is lista3? {lista1 is lista3}")   # True (mesmo objeto)

# 3.4. Pertinência em sequências (in e not in)
texto = "Python é incrível"
print(f"'é' in texto? {'é' in texto}")            # True, o caractere 'é' está na string
print(f"'Java' not in texto? {'Java' not in texto}")  # True, 'Java' não aparece no texto

frutas = ["maçã", "banana", "laranja"]
print(f"'banana' in frutas? {'banana' in frutas}")    # True
print(f"'uva' in frutas? {'uva' in frutas}")          # False
