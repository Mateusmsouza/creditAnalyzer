
#  CreditAnalyzer - Uma API estupidamente simples feita com TDD

##  Tecnologias usadas durante o desenvolvimento
- Python
- Starlette (Micro Web Framework)
- Pytest (Unit Tests)
  
## Aplicação
- A aplicação permite a solicitação de um cartão de crédito, o usuário insere suas informações básicas e o sistema irá fazer uma análise da liberação do cartão.
### Regras
Quando o usuário solicitar um cartão, há aprovação automática do sistema, sua regra será:

A partir do recebimento das informações básicas do usuário, e seu score (sendo de 1 a 999) sendo que, dependendo do score recebido a solicitação é aprovada ou não, também alterando o seu limite de crédito, que segue a seguinte lógica:

| Score     | Crédito                                        |
| --------- | ---------------------------------------------- |
| 1 a 299   | Reprovado                                      |
| 300 a 599 | R$1000,00                                      |
| 600 a 799 | 50% da renda informada, valor mínimo R$1000,00 |
| 800 a 950 | 200% da renda informada                        |
| 951 a 999 | Sem limites, considerar R$ 1.000.000           |

### Endpoints

- **[POST]** - /credit_analyze
