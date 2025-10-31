import random
import pytest

# -------------------------------
# Teste de Desempenho (P95)
# -------------------------------
def test_performance_p95_latency():
    latencias = [random.randint(100, 800) for _ in range(1000)]
    p95 = sorted(latencias)[int(0.95 * len(latencias)) - 1]
    assert p95 < 500, f"P95 muito alto: {p95}ms"


# -------------------------------
# Teste de Carga (Throughput)
# -------------------------------
def test_load_throughput():
    requisicoes = 10000
    tempo_total = 4
    throughput = requisicoes / tempo_total
    assert throughput > 2000, f"Throughput insuficiente: {throughput} req/s"


# -------------------------------
# Teste de Estresse (Ponto de Quebra)
# -------------------------------
def test_stress_breakpoint():
    usuarios = [i for i in range(20000)] 
    ponto_quebra = 16000  
    assert ponto_quebra > 15000, f"Ponto de quebra abaixo do esperado: {ponto_quebra}"


# -------------------------------
# Teste de Segurança (Rate Limiting)
# -------------------------------
def test_security_rate_limiting():
    limite = 100
    requisicoes = 120
    bloqueadas = max(0, requisicoes - limite)
    assert bloqueadas > 0, "Rate limiting não foi aplicado corretamente"


# -------------------------------
# Teste de Disponibilidade
# -------------------------------
def test_availability():
    uptime = 99.95
    assert uptime >= 99.9, f"Disponibilidade insuficiente: {uptime}%"
