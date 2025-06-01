# exemplo1.py
# 1) input("...") exibe uma mensagem na tela e espera o usuário digitar algo + Enter.
nome = input("Digite seu nome: ")

# 2) Agora 'nome' é uma string contendo o que o usuário digitou.
#    Podemos, então, usar essa variável normalmente.
print(f"Olá, {nome}! Seja bem-vindo(a)!")

# exemplo2.py
# 1) Pede ao usuário que digite a idade.
idade_str = input("Digite sua idade: ")

# 2) Convertemos a string para inteiro.
#    Se o usuário digitar algo que não seja número, vai gerar ValueError.
try:
    idade = int(idade_str)
except ValueError:
    print("Erro: Por favor, digite um número inteiro para a idade.")
    # Encerra o programa ou poderia pedir novamente, dependendo do fluxo.
    exit(1)

# 3) Calculamos quantos anos faltam para a pessoa completar 100 anos.
faltam = 100 - idade

# 4) Exibimos o resultado.
print(f"Você terá 100 anos em {faltam} anos.")

# exemplo3.py
# 1) Pede dois números separados por espaço, ex: "5 7"
entrada = input("Digite dois números inteiros separados por espaço: ")

# 2) split() retorna lista de strings, separando onde houver espaço (por padrão).
valores = entrada.split()

# 3) Se o usuário não digitar exatamente dois valores, avisamos e encerramos.
if len(valores) != 2:
    print("Erro: você deve informar exatamente dois números.")
    exit(1)

# 4) Convertendo cada valor para inteiro.
try:
    a = int(valores[0])
    b = int(valores[1])
except ValueError:
    print("Erro: ambos os valores devem ser números inteiros.")
    exit(1)

# 5) Calculamos e exibimos a soma.
soma = a + b
print(f"A soma de {a} e {b} é {soma}.")
