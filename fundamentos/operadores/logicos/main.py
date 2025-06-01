# ==================================================
#  Exemplos de Operadores Lógicos (and, or, not)
# ==================================================

# 4.1. AND: precisa que ambas as condições sejam verdadeiras
idade = 20
renda = 2500

# Para aprovar um cadastro é necessário ter idade >= 18 E renda >= 2000
if idade >= 18 and renda >= 2000:
    print("Cadastro aprovado (AND): idoso >=18 e renda >=2000")
else:
    print("Cadastro negado (AND)")

# 4.2. OR: precisa que pelo menos uma condição seja verdadeira
dia_semana = "domingo"

# O cinema abre no sábado OU no domingo
if dia_semana == "sábado" or dia_semana == "domingo":
    print("Cinema está aberto (OR).")
else:
    print("Cinema fechado (OR).")

# 4.3. NOT: nega a condição
usuario_ativo = False

if not usuario_ativo:
    print("O usuário NÃO está ativo.")
else:
    print("O usuário está ativo.")

# 4.4. Avaliação curta (short-circuit) evita erros
usuario = None

# Se uso AND: como 'usuario' é None, o segundo termo (usuario.is_admin) não é avaliado e não causa erro
if usuario and hasattr(usuario, "is_admin") and usuario.is_admin:
    print("Usuário é admin.")
else:
    print("Sem permissão ou usuário inexistente (short-circuit).")
