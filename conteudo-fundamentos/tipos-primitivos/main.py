# TIPOS PRIMITIVOS EM PYTHON - GUIA COMPLETO PARA BACKEND
# ========================================================

print("INTRODUÇÃO: Python e Tipos Dinâmicos")
print("=" * 50)

# Demonstração da tipagem dinâmica
variavel = 42
print(f"Valor: {variavel}, Tipo: {type(variavel)}")

variavel = "Agora sou texto"
print(f"Valor: {variavel}, Tipo: {type(variavel)}")

# IMPORTANTE: Evite mudanças de tipo em produção!
print("⚠️  Em produção, mantenha consistência de tipos!\n")

# =============================================================================
# 1. NÚMEROS INTEIROS (int) - FUNDAÇÃO DOS SISTEMAS BACKEND
# =============================================================================
print("1. NÚMEROS INTEIROS (int)")
print("-" * 30)

# Contextos típicos de backend
user_id = 1547  # IDs de usuários/recursos
status_code = 200  # Códigos de resposta HTTP
port = 8080  # Portas de servidor
timeout_seconds = 30  # Configurações de timeout

print(f"User ID: {user_id} (tipo: {type(user_id)})")
print(f"Status Code: {status_code}")
print(f"Server Port: {port}")

# Representações especiais (úteis em sistemas)
hexadecimal_id = 0xFF  # 255 em decimal - IDs em hex
octal_permission = 0o755  # Permissões de arquivo (Unix/Linux)
binary_flag = 0b1010  # 10 em decimal - flags de bits

print(f"Hex ID: {hexadecimal_id}")
print(f"File Permission: {octal_permission}")
print(f"Binary Flag: {binary_flag}")

# Python permite números inteiros de tamanho arbitrário!
big_user_count = 10 ** 15  # 1 quatrilhão de usuários (teoricamente)
print(f"Big Number: {big_user_count}")
print(f"Tamanho em bytes: {big_user_count.bit_length() // 8 + 1}")

print("\n")

# =============================================================================
# 2. NÚMEROS DECIMAIS (float) - CÁLCULOS E MEDIÇÕES
# =============================================================================
print("2. NÚMEROS DECIMAIS (float)")
print("-" * 30)

# Aplicações comuns em backend
price = 99.99  # Preços (cuidado com precisão!)
api_response_time = 0.247  # Tempos de resposta em segundos
cpu_usage = 78.5  # Percentual de uso de CPU
latitude = -23.5505  # Coordenadas geográficas
longitude = -46.6333

print(f"Preço: R$ {price}")
print(f"Tempo de resposta: {api_response_time}s")
print(f"Uso de CPU: {cpu_usage}%")
print(f"Localização: {latitude}, {longitude}")

# ATENÇÃO: Problemas de precisão com float!
print("\n⚠️  CUIDADO: Problemas de precisão financeira")
resultado_impreciso = 0.1 + 0.2
print(f"0.1 + 0.2 = {resultado_impreciso}")  # Não é exatamente 0.3!

# Para cálculos monetários, use Decimal (não é primitivo, mas importante)
from decimal import Decimal

preco_preciso = Decimal('99.99')
desconto = Decimal('10.00')
total = preco_preciso - desconto
print(f"Cálculo preciso: {total}")

print("\n")

# =============================================================================
# 3. STRINGS (str) - MANIPULAÇÃO DE DADOS TEXTUAIS
# =============================================================================
print("3. STRINGS (str) - Manipulação Textual")
print("-" * 40)

# Contextos típicos de backend
api_endpoint = "/api/v1/users"  # Rotas de API
database_url = "postgresql://localhost:5432/mydb"
jwt_token = "Bearer eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9..."
error_message = "Usuário não encontrado"
json_response = '{"status": "success", "data": []}'

print(f"Endpoint: {api_endpoint}")
print(f"DB URL: {database_url}")
print(f"Token: {jwt_token[:20]}...")  # Só mostra início por segurança

# Operações essenciais para backend
email = "walker.dev@example.com"

# Validações básicas com strings
is_valid_email = "@" in email and "." in email.split("@")[1]
print(f"Email válido? {is_valid_email}")

# Extração de dados (parsing simples)
token_clean = jwt_token[7:] if jwt_token.startswith("Bearer ") else jwt_token
print(f"Token limpo: {token_clean[:10]}...")

# Formatação para logs e respostas
request_id = "req_12345"
log_message = f"[{request_id}] Processando requisição para {api_endpoint}"
print(f"Log: {log_message}")

# Strings multilinha para SQL ou configurações
sql_query = """
SELECT u.id, u.name, u.email 
FROM users u 
WHERE u.active = true 
  AND u.created_at > %s
"""
print(f"SQL Query preparada: {sql_query.strip()}")

print("\n")

# =============================================================================
# 4. BOOLEANOS (bool) - CONTROLE LÓGICO E FLAGS
# =============================================================================
print("4. BOOLEANOS (bool) - Controle e Flags")
print("-" * 40)

# Estados de sistema e controle de fluxo
is_authenticated = True  # Status de autenticação
is_admin = False  # Permissões de usuário
service_enabled = True  # Flags de funcionalidade
debug_mode = False  # Configurações de ambiente
database_connected = True  # Status de conexões

print(f"Usuário autenticado: {is_authenticated}")
print(f"É administrador: {is_admin}")
print(f"Serviço habilitado: {service_enabled}")

# Lógica de negócio com booleanos
can_access_api = is_authenticated and service_enabled
can_delete_users = is_authenticated and is_admin

print(f"Pode acessar API: {can_access_api}")
print(f"Pode deletar usuários: {can_delete_users}")

# Conversões importantes (dados externos chegam como string!)
status_from_api = "true"  # Vem de JSON/form
status_bool = status_from_api.lower() == "true"
print(f"Status convertido: {status_bool}")

# Valores "truthy" e "falsy" - importante para validações
valores_falsy = [False, 0, "", [], {}, None]
valores_truthy = [True, 1, "texto", [1], {"key": "value"}, 42]

print("Valores falsy:", [bool(v) for v in valores_falsy])
print("Valores truthy:", [bool(v) for v in valores_truthy])

print("\n")

# =============================================================================
# 5. NONE (NoneType) - AUSÊNCIA DE VALOR
# =============================================================================
print("5. NONE (NoneType) - Ausência de Valor")
print("-" * 40)

# Inicialização de variáveis
user_session = None  # Sessão ainda não criada
cached_data = None  # Cache ainda não populado
last_error = None  # Nenhum erro registrado

print(f"Sessão: {user_session}")
print(f"Cache: {cached_data}")


# Função que pode retornar None (comum em backends)
def find_user_by_email(email):
    """Simula busca no banco - pode não encontrar usuário"""
    if email == "walker@example.com":
        return {"id": 1, "name": "Walker", "email": email}
    return None  # Usuário não encontrado


# Testando a função
user_found = find_user_by_email("inexistente@example.com")
print(f"Usuário encontrado: {user_found}")

# Verificação segura de None (sempre use 'is', não '==')
if user_found is None:
    print("✓ Usuário não encontrado - tratamento adequado")
else:
    print(f"Usuário: {user_found['name']}")

# None em estruturas de dados (valores opcionais)
user_profile = {
    "name": "Walker",
    "email": "walker@example.com",
    "phone": None,  # Campo opcional
    "avatar": None  # Ainda não enviado
}

print(f"Perfil: {user_profile}")

print("\n")

# =============================================================================
# 6. CONVERSÕES E VALIDAÇÕES - ESSENCIAL PARA BACKEND
# =============================================================================
print("6. CONVERSÕES E VALIDAÇÕES - Essencial para Backend")
print("-" * 55)

# Simulando dados vindos de uma API/formulário (sempre strings!)
api_data = {
    "user_id": "1547",
    "age": "28",
    "salary": "5500.50",
    "is_active": "true",
    "last_login": "null"
}

print("Dados recebidos da API:")
for key, value in api_data.items():
    print(f"  {key}: {value} (tipo: {type(value)})")


# Conversão segura com tratamento de erros
def safe_convert_to_int(value):
    """Converte valor para int de forma segura"""
    try:
        return int(value) if value and value != "null" else None
    except (ValueError, TypeError):
        return None


def safe_convert_to_float(value):
    """Converte valor para float de forma segura"""
    try:
        return float(value) if value and value != "null" else None
    except (ValueError, TypeError):
        return None


def safe_convert_to_bool(value):
    """Converte valor para bool de forma segura"""
    if isinstance(value, str):
        return value.lower() in ("true", "1", "yes", "on")
    return bool(value)


# Aplicando conversões
user_id = safe_convert_to_int(api_data["user_id"])
age = safe_convert_to_int(api_data["age"])
salary = safe_convert_to_float(api_data["salary"])
is_active = safe_convert_to_bool(api_data["is_active"])
last_login = None if api_data["last_login"] == "null" else api_data["last_login"]

print("\nDados convertidos:")
print(f"  user_id: {user_id} (tipo: {type(user_id)})")
print(f"  age: {age} (tipo: {type(age)})")
print(f"  salary: {salary} (tipo: {type(salary)})")
print(f"  is_active: {is_active} (tipo: {type(is_active)})")
print(f"  last_login: {last_login} (tipo: {type(last_login)})")

print("\n")

# =============================================================================
# 7. EXEMPLO PRÁTICO: PROCESSAMENTO DE REQUISIÇÃO API
# =============================================================================
print("7. EXEMPLO PRÁTICO: Processamento de Requisição API")
print("-" * 55)

# Simulando uma requisição POST para criar produto
incoming_request = {
    "product_name": "Notebook Gamer",
    "price": "2999.99",
    "quantity": "5",
    "is_available": "true",
    "category_id": "42",
    "description": "Notebook para jogos de alta performance",
    "discount_percent": "10.5"
}

print("📥 Requisição recebida:")
for key, value in incoming_request.items():
    print(f"  {key}: {value}")

# Validação e conversão (código típico de backend)
errors = []
processed_data = {}

# Validar e converter cada campo
try:
    # String obrigatória
    if not incoming_request.get("product_name"):
        errors.append("Nome do produto é obrigatório")
    else:
        processed_data["product_name"] = incoming_request["product_name"]

    # Float obrigatório (preço)
    price_str = incoming_request.get("price")
    if not price_str:
        errors.append("Preço é obrigatório")
    else:
        try:
            price = float(price_str)
            if price <= 0:
                errors.append("Preço deve ser positivo")
            else:
                processed_data["price"] = price
        except ValueError:
            errors.append("Preço deve ser um número válido")

    # Int obrigatório (quantidade)
    quantity_str = incoming_request.get("quantity")
    if not quantity_str:
        errors.append("Quantidade é obrigatória")
    else:
        try:
            quantity = int(quantity_str)
            if quantity < 0:
                errors.append("Quantidade não pode ser negativa")
            else:
                processed_data["quantity"] = quantity
        except ValueError:
            errors.append("Quantidade deve ser um número inteiro")

    # Boolean
    is_available = safe_convert_to_bool(incoming_request.get("is_available", "false"))
    processed_data["is_available"] = is_available

    # Int opcional
    category_id = safe_convert_to_int(incoming_request.get("category_id"))
    processed_data["category_id"] = category_id

    # String opcional
    processed_data["description"] = incoming_request.get("description")

    # Float opcional (desconto)
    discount = safe_convert_to_float(incoming_request.get("discount_percent", "0"))
    processed_data["discount_percent"] = discount

except Exception as e:
    errors.append(f"Erro inesperado: {str(e)}")

# Resultado do processamento
print("\n📋 Resultado do processamento:")
if errors:
    print("❌ Erros encontrados:")
    for error in errors:
        print(f"  - {error}")
else:
    print("✅ Dados válidos e convertidos:")
    for key, value in processed_data.items():
        print(f"  {key}: {value} (tipo: {type(value)})")

    # Calcular preço final (exemplo de uso dos tipos convertidos)
    if "price" in processed_data and "discount_percent" in processed_data:
        final_price = processed_data["price"] * (1 - processed_data["discount_percent"] / 100)
        print(f"\n💰 Preço final: R$ {final_price:.2f}")

print("\n")

# =============================================================================
# 8. DICAS CRUCIAIS PARA DESENVOLVIMENTO BACKEND
# =============================================================================
print("8. DICAS CRUCIAIS PARA BACKEND")
print("-" * 35)

print("""
🚨 REGRA DE OURO: Sempre valide e converta dados externos!

✅ BOAS PRÁTICAS:
• Use 'is None' em vez de '== None'
• Implemente conversão segura com try/except
• Para dinheiro, considere usar Decimal em vez de float
• Valide tipos antes de usar em operações críticas
• Mantenha consistência de tipos em funções

❌ EVITE:
• Mudanças de tipo na mesma variável em produção
• Assumir que dados externos estão no tipo correto
• Operações matemáticas diretas com dados não validados
• Comparações de float para igualdade exata

🔧 PARA LEMBRAR:
• Python: tipagem dinâmica, mas seja disciplinado
• Todos os primitivos são imutáveis
• None representa ausência de valor
• Booleanos controlam fluxo de negócio
• Strings são Unicode por padrão
""")
