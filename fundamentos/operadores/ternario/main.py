# ================================================
#  Exemplos de Operador Ternário (if-else em 1 linha)
# ================================================

# 5.1. Exemplo simples: classificar nota como Aprovado/Reprovado
nota = 7.5
resultado = "Aprovado" if nota >= 6 else "Reprovado"
print(f"Com nota {nota}, o aluno foi {resultado}.")

# 5.2. Verificar desconto com ternário
valor_compra = 150.0
desconto = 0.10 if valor_compra >= 100 else 0   # 10% de desconto se >=100
valor_final = valor_compra - (valor_compra * desconto)
print(f"Valor da compra: R${valor_compra:.2f}. Desconto: {desconto*100:.0f}%. Valor final: R${valor_final:.2f}.")

# 5.3. Uso em list comprehension para marcar números pares/ímpares
numeros = [1, 2, 3, 4, 5, 6]
labels_paridade = ["Par" if num % 2 == 0 else "Ímpar" for num in numeros]
print("Números:", numeros)
print("Paridade:", labels_paridade)

# 5.4. Ternário aninhado (não recomendado se ficar muito complexo)
x = 8
mensagem = "Divisível por 4" if x % 4 == 0 else ("Divisível por 2" if x % 2 == 0 else "Não divisível por 2 ou 4")
print(f"Para x = {x}, resultado: {mensagem}")
