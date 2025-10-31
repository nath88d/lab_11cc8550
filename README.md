Gabriel Destro 24.122.059-9 <br>
Nathan Dantas 24.122.041-7
# Plano de Teste Integrado – Testes Não Funcionais

##  Requisitos e Metas do Sistema

**Requisitos principais:**

* Usuários simultâneos esperados: **10.000**
* Tempo de resposta (P95): **< 500 ms** para 95% das requisições
* Disponibilidade: **≥ 99.9%** durante o evento
* Throughput sustentado: **> 2000 req/s**
* Ponto de quebra (estresse): **> 15.000 usuários**
* Eficiência horizontal: **> 80%**
* Rate limiting: **100 req/min/IP**

---

## Tipos de Teste e Objetivos

O plano contempla os seguintes **testes não funcionais**:

* **Desempenho:** latências e percentis (P50, P95, P99).
* **Carga:** throughput sustentado e estabilidade.
* **Estresse:** identificar o ponto de quebra de performance.
* **Escalabilidade:** eficiência ao adicionar instâncias.
* **Segurança:** verificar aplicação do rate limiting e resistência a ataques.

---

## Execução

1. **Desempenho:**

   * Simulação com 10.000 usuários.
   * Latência média e P95/P99 das requisições principais.

2. **Carga:**

   * Estabilidade durante 30 a 60 minutos com taxa constante de requisições.
   * Medir throughput sustentado (>2000 req/s) e taxa de erro.

3. **Estresse:**

   * Ramp-up progressivo até degradação do sistema.
   * Determinar o ponto de quebra (>15.000 usuários).

4. **Segurança:**

   * Simular IP enviando 500 requisições/minuto.
   * Bloqueio após 100 requisições.

---

## Resultados Simulados e Métricas

| Tipo             | Métrica                 | Meta           | Status |
| ---------------- | ----------------------- | -------------- | ------ |
| Desempenho (P95) | P95 latency (ms)        | < 500 ms       | Desaprovado |
| Carga            | Throughput (req/s)      | > 2000 req/s   | Aprovado |
| Estresse         | Ponto de quebra (users) | > 15000 users  | Aprovado |
| Segurança        | Rate limiting           | 100 req/min/IP | Aprovado |
| Disponibilidade  | Availability (%)        | ≥ 99.9%        | Aprovado |
| Desempenho (P99) | P99 latency (ms)        | < 1000 ms      | Desaprovado |

---

## **Resumo de aprovação:**

*  **APROVADO:** Carga, Estresse, Segurança, Disponibilidade
*  **DESAPROVADO:** Desempenho (P95, P99) 
