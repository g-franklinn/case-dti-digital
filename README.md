# Teste Prático - Processo Seletivo DTI Digital - Estágio Dados

## Visão Geral

Este repositório contém a solução completa para o teste prático do processo seletivo para o estágio em Data & Analytics da DTI Digital. O projeto foi desenvolvido com o objetivo de não apenas resolver os problemas propostos, mas também de demonstrar a aplicação de boas práticas de engenharia de software e dados, incluindo organização de projeto, versionamento de código, clareza, testes automatizados e reprodutibilidade.

---

##  Estrutura do Projeto

O projeto foi organizado em uma estrutura de diretórios para separar as diferentes responsabilidades (código-fonte, testes, dados, etc.).

```
case-dti-digital/
│   
├── data/
│   ├── dados.csv           # Dados referentes à questão 2
│   ├── clientes.csv        # Dados da tabela clientes
│   ├── produtos.csv        # Dados da tabela produtos
│   └── vendas.csv          # Dados da tabela vendas
|
├── src/
│   ├── python/             # Soluções em Python
│   │   ├── questao2a.py
│   │   └── questao2b.py
│   ├── spark/              # Soluções em PySpark
│   │   ├── questao3a.py
│   │   └── questao3b.py
│   └── sql/                # Soluções em SQL
│       ├── questao1a.sql
│       ├── questao1b.sql
│       └── questao1c.sql
├── tests/
│   ├── test_questao2a.py  # Testes unitários para a questão 2a
│   └── test_questao2b.py  # Testes unitários para a questão 2b
│
├── .gitignore              # Arquivo para ignorar arquivos não versionados
├── pytest.ini              # Arquivo de configuração do PyTest
├── README.md               # Esta documentação
└── requirements.txt        # Dependências do projeto Python
```

---

## Boas Práticas 

Esta seção detalha as escolhas técnicas e as práticas de desenvolvimento adotadas no projeto.

### Git Workflow
* **Branches:** Todo o desenvolvimento foi feito em uma *feature branch*, seguindo a prática de nunca trabalhar diretamente na branch `main`. A nomenclatura `tipo/descricao` (ex: `feat/solve-case`) foi usada para dar clareza à intenção da branch.
* **Commits Atômicos:** O histórico do projeto foi construído com o conceito **commits atômicos**, onde cada commit representa uma questão feita (ex: "feat: add question1 solutions"). Foi utilizada a convenção *Conventional Commits* (`feat`, `fix`, `test`, `docs`) para padronizar as mensagens, facilitando a leitura e a automação de changelogs.

### Clean Code
Foi adotada uma preocupação com a escrita de um código limpo, focando em:
* **Nomenclatura Clara:** Variáveis e funções foram nomeadas com cuidado para que o código seja o mais autoexplicativo possível.
* **Comentários:** Os comentários foram utilizados apenas quando necessário para melhor legibilidade do código, evitando poluição visual e redundância.

### Testes Unitários
A adição de testes unitários com `pytest` é fundamental para garantir a qualidade e a manutenibilidade do código. Eles:
* **Garantem a Lógica:** Provam que as funções se comportam como esperado em diferentes cenários.
* **Previnem Regressões:** Permitem que futuras alterações no código sejam feitas com a segurança de que não quebramos algo que já funcionava.
* **Atuam como Documentação:** O arquivo de teste serve como um exemplo prático de como a função deve ser utilizada.

### Tomadas de Decisão nas Questões

#### Questão 1: SQL
* **Lógica da Questão 1c:** A consulta para encontrar clientes que compraram de todas as categorias foi resolvida comparando a contagem de categorias distintas por cliente com a contagem total de categorias da loja, utilizando a cláusula `HAVING` para filtrar os grupos após a agregação.

#### Questão 2: Python
* **Questão 2a (Mediana):**
    * O uso de *Type Hints* (`List`, `Union`) funciona como um "contrato" para a função, melhorando a clareza e permitindo que ferramentas de análise estática encontrem bugs antes da execução. A lista pode receber `int` e `float` para ser mais flexível. O tipo de retorno é `Union[int, float]` porque a mediana de uma lista de inteiros pode resultar em um `float` (ex: a mediana de `[2, 4]` é `3.0`).
* **Questão 2b (Filtro de CSV):**
    * **Uso do Pandas:** A biblioteca **Pandas** foi escolhida por ser o padrão da indústria para manipulação de dados em Python, oferecendo operações de leitura, filtragem e escrita.
    * **Uso de Constantes:** Constantes como `AGE_THRESHOLD` foram utilizadas para tornar o script mais legível e fácil de manter.

#### Questão 3: Spark
* **Tabela `clientes` na Questão 3b:** Conforme o enunciado pedia para ler as três tabelas, o DataFrame `df_clients` foi carregado. No entanto, para o cálculo da maior receita por categoria de produto, suas informações não eram necessárias.

#### Questão 4: Git
* Todas as tomadas de decisão deste projeto, no que tange a versionamento de código, foram feitas com as práticas descritas na questão 4, cuja resposta se encontra no arquivo `README.md` em sua respectiva pasta. 
