qtd_vendas_coca = 150
qtd_vendas_pepsi = 130
preco_unitario_coca = 1.50
preco_unitario_pepsi = 1.50
custo_loja = 2500.00

#1. Qual foi o faturamento de Pepsi da Loja?
faturamento_pepsi = preco_unitario_pepsi * qtd_vendas_pepsi
print(f"O faturamento da Pepsi foi de {faturamento_pepsi}")
#2. Qual foi o faturamento de Coca da Loja?"""
faturamento_coca = preco_unitario_coca * qtd_vendas_coca
print(f"O faturamento da Coca foi de {faturamento_coca}")
#3. Qual foi o Lucro da loja?"""
faturamento_total = faturamento_coca + faturamento_pepsi
lucro = faturamento_total - custo_loja
print(f"O lucro da loja foi {lucro}")
#4. Qual foi a Margem da Loja? (Lembre-se, margem = Lucro / Faturamento). Não precisa formatar em percentual"""
margem = lucro / faturamento_total
print(margem)

