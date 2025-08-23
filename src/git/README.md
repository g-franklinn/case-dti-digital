## Respostas Teóricas - Git

### a)  Explique o que é um branch no Git e qual a sua utilidade.

Uma **branch**, ou ramificação no Git é um ponteiro móvel para um dos commits do seu histórico. Ele funciona como uma linha de desenvolvimento independente, permitindo que você trabalhe em novas funcionalidades, correções de bugs ou experimentos sem afetar a linha principal de código.<br>

Sua utilidade principal consiste em garantir **isolamento**, **desenvolvimento paralelo** e **fluxos de trabalho organizados**. Isso significa a possibilidade de múltiplas pessoas trabalharem em diferentes partes do projeto simultaneamente, sem interferir uns nos outros. Além disso, as branches facilitam práticas como *Code Review* através de *Pull Requests*, onde as alterações de um branch são revisadas antes de serem integradas (`merge`) à branch `main`.


### b) Descreva o fluxo de trabalho típico para adicionar, commitar e enviar (push) suas alterações para um repositório remoto no Git. L️iste os comandos utilizados. 

O fluxo de trabalho fundamental para salvar e compartilhar alterações no Git segue três estágios:

1.  **`git add` (Adicionar à Staging Area):**
    - **Função:** Move as alterações do seu diretório de trabalho (onde você edita os arquivos) para uma área de preparação chamada *Staging Area*. Isso permite que você escolha exatamente quais alterações farão parte do próximo "pacote" (commit).
    - **Comando:** `git add <nome_do_arquivo>` ou `git add .` para adicionar todos os arquivos alterados.


2.  **`git commit` (Salvar no Repositório Local):**
    - **Função:** Cria um *snapshot* permanente das alterações que estão na *Staging Area* e o salva no seu repositório local. A mensagem é essencial para manter um histórico claro do projeto.
    - **Comando:** `git commit -m "Mensagem descritiva da alteração"`
    

3.  **`git push` (Enviar para o Repositório Remoto):**
    - **Função:** Envia seus commits locais para um repositório remoto (como GitHub, GitLab), tornando suas alterações visíveis e acessíveis para outros colaboradores.
    - **Comando:** `git push <remoto> <branch>` (ex: `git push origin feat/solve-case `)

Além disso, como descrito na *letra a*, anteriormente, antes de fazer esses procedimentos é necessário trabalhar em uma branch separada para a tarefa designada. Para isso, utiliza-se o comando: `git checkout -b <nome-da-branch>` , de modo a criar e acessar uma nova branch a partir de outra já existente. Esse comando também permite ao usuário acessar outras branches já existentes, para isso, é necessário apenas remover a flag `-b` do comando.


### Boas Práticas.

Para melhor organização, individual ou entre os colaboradores do código, existem boas práticas de padronização nas mensagens de commit e nome das branches. Essas práticas facilitam a leitura do histórico do projeto, reduzem ambiguidades e tornam mais simples o processo de revisão e integração de código.<br>

Algumas palavras comumente utilizadas nesse contexto são `feat`, `fix` ou `chore`, que servem, respectivamente para adicionar uma nova funcionalidade ao código, corrigir bugs ou configurações ou atualização de dependências. (ex: `git commit -m "docs: add question4 solutions"`)