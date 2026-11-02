# Avaliação A2 - Paradigmas de Linguagens de Programação

> Este arquivo é o esqueleto do **README.md** do repositório GitHub do seu grupo.
> A Entrega deve ser feita exclusivamente pelo envio do link desse repositório.
> Quaisquer instruções anteriores em desacordo com esta devem ser ignoradas
> Preencha cada seção abaixo. Não altere a ordem e nem apague os títulos — apenas substitua os placeholders pelo conteúdo do seu projeto.

**Grupo 05** <!-- Substitua XX pelo número do seu grupo -->

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

> ⚠️ **Aviso:** O código deve rodar exclusivamente em ambiente online, sem necessidade de instalação local.

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
O problema foi resolvido por meio da modelagem de uma árvore genealógica utilizando uma base de conhecimento em Prolog (com fatos de progenitor e sexo e regras lógicas de parentesco) e sua respectiva tradução para a Orientação a Objetos em Python.

Na implementação lógica, foram estabelecidas regras para identificar pais, mães, irmãos, irmãs, avós, tios, tias (incluindo cônjuges/afins) e primos, incorporando predicados de agregação como setof/3 para evitar duplicações decorrentes do backtracking gerado pela dupla ascendência (pai e mãe).

Na contraparte em Python, a solução estruturou os dados em conjuntos (sets) e dicionários (dicts) encapsulados na classe ArvoreGenealogica, oferecendo métodos dinâmicos de busca (buscar_parentes), tratamento de strings e menus interativos de terminal, além de relatórios textuais verticais para exibir todas as relações de um indivíduo simultaneamente.

### Análise Comparativa

### 1. Sintaxe
O Prolog adota um paradigma estritamente declarativo, onde o desenvolvedor declara fatos e regras de relação (ex: filho_de(X, Y) :- progenitor(Y, X).) e o motor de inferência resolve as consultas. O Python adota o paradigma imperativo e orientado a objetos, exigindo o controle procedural explícito do fluxo de execução. Enquanto a verificação de parentesco em Prolog ocorre por unificação direta de variáveis nas regras lógicas, em Python é necessário escrever compreensões de listas ou varreduras condicionais explícitas.

Ex:



### 2. Semântica
Tipos e Avaliação: O Prolog baseia-se na lógica de predicados e unificação de termos, operando com avaliação orientada a busca e backtracking automático. O Python utiliza tipagem dinâmica, atribuição explícita de variáveis e avaliação estritamente sequencial.

Escopo e Comportamento: As regras em Prolog possuem bidirecionalidade natural (uma mesma regra serve para buscar descendentes ou ascendentes dependendo de quais variáveis estão instanciadas). Em Python, os métodos exigem parâmetros direcionados e lógica de filtragem programada via funções lambda e dicionários de mapeamento.

### 3. Gerenciamento de Memória
Mecanismos internos: O Prolog gerencia a memória internamente através de sua base de dados dinâmica e pilhas de execução para o mecanismo de retrocesso (backtracking). O Python utiliza um coletor de lixo (garbage collector) baseado em contagem de referências e alocação dinâmica de objetos em tempo de execução.

Comparação com o C: Diferente da linguagem C, onde o desenvolvedor precisa gerenciar explicitamente a alocação e liberação de memória com malloc e free, tanto o Prolog quanto o Python abstraem totalmente essa complexidade de baixo nível.

### 4. Trade-offs
Vantagens do Prolog: Excelente para expressar relações complexas de forma extremamente concisa, delegando a complexidade da busca e unificação ao interpretador da linguagem.

Desvantagens do Prolog: Curva de aprendizado íngreme, controle de fluxo menos intuitivo (comportamento de backtracking que pode gerar repetições e exige tratamento com setof/3), e maior dificuldade para criar interfaces textuais dinâmicas ou menus interativos complexos.

Vantagens do Python: Elevada facilidade para estruturar menus interativos no terminal, manipulação robusta de textos/strings (.lower().strip()), formatação de saídas estruturadas e integração flexível com sistemas modernos.

Desvantagens do Python: Demanda um volume muito maior de código imperativo e lógica procedural para implementar regras que no Prolog são deduzidas de forma puramente declarativa.

### Resumo da Análise Comparativa
*Compare a linguagem/paradigma estudado com os que você já domina (C, Java ou Python). O detalhamento completo deve estar no PDF, mas inclua os pontos principais aqui.*

*   **Sintaxe:** (O que muda na forma de escrever a solução?)
*   **Semântica:** (Tipos, escopo, forma de avaliação - ex: estrita vs. preguiçosa, unificação vs. atribuição)
*   **Gerenciamento de Memória:** (Coleta de lixo automática vs. gerenciamento manual)
*   **Trade-offs:** (Vantagens e desvantagens do novo paradigma em relação aos anteriores)

## Log de Uso de Inteligência Artificial (IA)
*O uso de IA (ChatGPT, Claude, Gemini, etc.) é permitido e incentivado para aprendizado, mas deve ser documentado. Preencha o log abaixo:*

*   **O que foi pedido à IA:** [Descreva os prompts ou dúvidas enviadas]
*   **Qual IA foi utilizada:** [Descreva modelo e versão. Exemplo: 'Anthropic Claude Fable 5.1']
*   **O que foi aproveitado:** [Descreva quais partes de código, lógicas ou explicações foram utilizadas]
*   **O que foi reescrito/entendido pelo grupo:** [Como o grupo adaptou a resposta da IA e o que aprenderam com isso. Lembre-se: qualquer integrante pode ser questionado no seminário.]
