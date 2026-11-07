# Avaliação A2 - Paradigmas de Linguagens de Programação

**Grupo 05** 

## 👥 Integrantes (3 a 5 alunos)
- Gustavo da Costa Matsuo (33646155)
- Kauã Covo Vieira (33928053)
- Luiz Gustavo Caldeira Ribeiro (33051925)
- Maria Isabella Nashimoto de Andrade (34101012)
- Paulo Henrique Santos Souza (33790671)

## Definição do Tema
- **Paradigma:** Lógico
- **Linguagem:** Prolog
- **Código do Tema:** L1
- **Descrição do Desafio:** Base de conhecimento genealógica

## Execução do Código

- **Ambiente Online Utilizado:**  SWISH 
- **Permalink:** [https://swish.swi-prolog.org/p/ArvoreGenealogicaProlog.pl]

### Instruções de Teste (Entrada e Saída)
Ao clicar no link e abrir a tela do ambiente online, haverá um espaço de digitação no canto inferior direito que possui ?-.
Nesta área, escreva: " mostrar_relacoes(). ".

Dentro do parênteses, escreva o nome de uma pessoa que esteja na árvore para verificar quais relações a pessoa tem dentro da
árvore.

Após isso, aparecerá logo abaixo a opção RUN, clique nele e o código retornará com quais pessoas o nome digitado tem relação e
qual o tipo de parentesco.

**Entrada de Exemplo:**
```text
mostrar_relacoes(nicole).
```

**Saída Esperada:**
```text
Pessoa: nicole
Parentes:
  Pai: diego
  Mãe: sarah
  Esposo(a): [yuri]
  Filhos: [samira]
  Irmãos: [leonardo]
  Irmãs: Nenhum
  Avô: [davi]
  Avó: [antonella]
  Tios: Nenhum
  Tias: Nenhum
  Primos: Nenhum
```

## Relatório Técnico

### Descrição da Solução
O problema proposto foi resolvido por meio da modelagem e implementação de uma árvore genealógica utilizando duas abordagens distintas para fins comparativos: o paradigma lógico baseado em regras no Prolog e o paradigma orientado a objetos em Python.

**1. Modelagem da Base de Conhecimento e Estrutura de Dados**
Em Prolog: A base de fatos foi estruturada utilizando o predicado binário progenitor(PaiOuMae, Filho) para registrar de forma unívoca a ascendência entre os indivíduos, complementada pelo fato estático sexo(Pessoa, Genero) para classificar rigidamente cada indivíduo como masculino ou feminino.

Em Python: A arquitetura encapsulou os dados dentro de uma classe dedicada (ArvoreGenealogica), armazenando as relações de parentesco em conjuntos estruturados (set de tuplas (progenitor, filho)) e os atributos demográficos em dicionários de mapeamento rápido (dict).

**2. Arquitetura de Regras Lógicas e Relações Derivadas**
A partir dos fatos básicos, construiu-se uma hierarquia modular de regras lógicas:

Parentescos Primários e Diretos: Definição de regras para pai/2, mae/2 e filho_de/2 por meio da inversão e filtragem de gênero sobre os fatos de progenitor.

Irmandade e Correção de Duplicatas por Dupla Ascendência: Como cada indivíduo possui nativamente dois progenitores (pai e mãe), consultas diretas geram duplicações por backtracking. Para solucionar isso, desenvolveu-se o predicado intermediário irmao_base/2, que valida o compartilhamento de progenitores, refinando-se depois em irmao/2 e irma/2. O uso da biblioteca nativa setof/3 garantiu o agrupamento e eliminação de duplicatas.

Ascendência Estendida e Colaterais: Implementação de regras para avós (vô/2, vó/2), tios consanguíneos e tios por afinidade (incorporando a regra de conjuge/2 baseada em filhos em comum) e primos (primo/2).

**3. Automatização de Relatórios Textuais Verticais**
Para atender ao requisito de exibir todas as relações de um indivíduo de uma só vez, implementou-se o predicado unificado mostrar_relacoes/1 em Prolog (análogo à Opção 2 do menu interativo em Python). Este algoritmo varre de forma limpa todas as categorias de parentesco e imprime um relatório estruturado no terminal.

### Análise Comparativa

### 1. Sintaxe
O Prolog adota um paradigma estritamente declarativo, onde o desenvolvedor declara fatos e regras de relação (ex: filho_de(X, Y) :- progenitor(Y, X).) e o motor de inferência resolve as consultas. O Python adota o paradigma imperativo e orientado a objetos, exigindo o controle procedural explícito do fluxo de execução. Enquanto a verificação de parentesco em Prolog ocorre por unificação direta de variáveis nas regras lógicas, em Python é necessário escrever compreensões de listas ou varreduras condicionais explícitas.
**Olhar Imagens 1 e 2 do repositório.**



### 2. Semântica
Tipos e Avaliação: O Prolog baseia-se na lógica de predicados e unificação de termos, operando com avaliação orientada a busca e backtracking automático. O Python utiliza tipagem dinâmica, atribuição explícita de variáveis e avaliação estritamente sequencial.

Escopo e Comportamento: As regras em Prolog possuem bidirecionalidade natural (uma mesma regra serve para buscar descendentes ou ascendentes dependendo de quais variáveis estão instanciadas). Em Python, os métodos exigem parâmetros direcionados e lógica de filtragem programada via funções lambda e dicionários de mapeamento.

### 3. Gerenciamento de Memória

O Prolog gerencia a memória internamente através da sua base de dados dinâmica de fatos e pilhas de execução de pilhas/trilhas (trail and local stacks) necessárias para suportar o mecanismo de backtracking.

O Python (CPython) gerencia memória por meio de alocação dinâmica em heap combinada com um coletor de lixo (garbage collector) baseado primordialmente em contagem de referências e detecção de ciclos.

Comparação com o C: Ao contrário da linguagem C — onde o programador é responsável pelo gerenciamento manual de ponteiros e chamadas explícitas a funções como malloc() e free() —, tanto o Prolog quanto o Python abstraem totalmente essa complexidade de baixo nível, eliminando riscos diretos de vazamentos de memória (memory leaks).

### 4. Trade-offs
Vantagens do Prolog: Extrema concisão e poder expressivo para modelar domínios complexos baseados em relações e restrições lógicas, desonerando o programador de escrever algoritmos de busca manuais.

Desvantagens do Prolog: Curva de aprendizado íngreme, controle de fluxo opaco (o comportamento de backtracking pode gerar repetições indesejadas que exigem tratamento com setof/3), e menor flexibilidade para construir interfaces de usuário ou menus interativos complexos.

Vantagens do Python: Excelente legibilidade, facilidade robusta para gerenciar entradas e saídas via terminal (menus interativos), tratamento avançado de strings (.lower().strip()) e facilidade de integração com ecossistemas de software modernos.

Desvantagens do Python: Exige um volume consideravelmente maior de código imperativo e lógica procedural para resolver problemas de inferência que no Prolog são deduzidos de forma nativa e declarativa.

### Resumo da Análise Comparativa

*   **Sintaxe:** O Prolog é declarativo baseando-se no que se deseja resolver por meio de fatos e regras lógicas, delegando a busca ao motor de inferência. O Python adota um estilo imperativo e orientado a objetos, exigindo algoritmos procedurais explícitos para percorrer estruturas.
  
*   **Semântica:** 

*   **Gerenciamento de Memória:**
No Prolog: o gerenciamento é automático e feito pela máquina abstrata da linguagem (como a WAM — Warren Abstract Machine), alocando pilhas temporárias para controlar os estados de backtracking e a base de fatos dinâmicos.
No Python: é utilizada a coleta de lixo (Garbage Collection) baseada primordialmente em contagem de referências suplementada por detecção de ciclos para objetos no heap.
Em comparação com o C que exige liberação manual com free e alocação com malloc, tanto o Prolog quanto o Python abstraem o gerenciamento de baixo nível para o programador.
*   **Trade-offs:** (Vantagens e desvantagens do novo paradigma em relação aos anteriores)

## Log de Uso de Inteligência Artificial (IA)


*   **O que foi pedido à IA:**

1- Foi pedido que a IA fizesse uma análise no código com a montagem da árvore, para verificar se havia irregularidades na sua construção.

2- Auxiliar na montagem de algoritmos para mapear os parentescos disponíveis por um determinado indivíduo e extrair as suas relações(pai, mãe, tios, primos, irmãos, entre outros).

3- Corrigir o código para evitar duplicatas no resultados do código.

4- Montar a mesma árvore e os algoritmos feitos na linguagem Prolog, em Python.

*   **Qual IA foi utilizada:** Google Gemini
*   **O que foi aproveitado:** Foi levado em conta os algoritmos feitos pela IA, após ser testado cada um deles, além das explicações feitas para ajudar o grupo a entender o código como um todo.
*   **O que foi reescrito/entendido pelo grupo:** A IA auxiliou no aprendizado da linguagem por meio de comentários, códigos e link de vídeos do YouTube, visto que era o primeiro contato do grupo com a linguagem. Foi analisado cada um dos códigos sugeridos pela IA para a resolução do problema proposto e rodados no ambiente online (Swi-Prolog).
