# Parte 1 - Operações e Variáveis
# Crie um programa que imprima (print) os principais indicadores da loja Hashtag&Drink no último ano.
# Obs: faça tudo usando variáveis.
#
# Valores do último ano:
# Quantidade de Vendas de Coca = 150
# Quantidade de Vendas de Pepsi = 130
# Preço Unitário da Coca = 1,50
# Preço Unitário da Pepsi = 1,50
# Custo da Loja: 2.500,00
#
# Use o bloco abaixo para criar todas as variáveis que precisar.
#
# 4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual
quantidade_vendas_da_pepsi = 130
preco_unitario_da_pepsi = 1.50
quantidade_vendas_da_coca = 180
preco_unitario_da_coca= 1.50
custo_da_loja = 2500.00

faturamento_da_loja_com_pepsi = quantidade_vendas_da_pepsi * preco_unitario_da_pepsi
faturamento_da_loja_com_coca = quantidade_vendas_da_coca * preco_unitario_da_coca
faturamento_total_da_loja = faturamento_da_loja_com_pepsi + faturamento_da_loja_com_coca

lucro_da_loja = faturamento_total_da_loja - custo_da_loja
margem_da_loja = lucro_da_loja / faturamento_total_da_loja

print(f"Margem da loja: {margem_da_loja}")