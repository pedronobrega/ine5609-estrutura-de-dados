# Trabalho II de Estrutura de Dados

- ## Lista duplamente encadeada

---

### Desenvolvedores

- Pedro Henrique Dias Nobrega

### Descrição

Esse trabalho é simples e está diretamente relacionado com as atividades que iniciamos em aula com a lista duplamente encadeada COM cursor.

As operações públicas que precisam estar implementadas são (no mínimo):

- `<elemento>` acessarAtual()
- `void` InserirAntesDoAtual ( novo )
- `void` InserirApósAtual ( novo )
- `void` inserirNoFim ( novo )
- `void` inserirNaFrente ( novo )
- `void` inserirNaPosicao ( k, novo )
- `void` ExcluirAtual ()
- `void` ExcluirPrim ()
- `void` ExcluirUlt ()
- `void` ExcluirElem ( chave )
- `void` ExcluirDaPos ( k )
- `boolean` Buscar ( chave )

As operações para controle do cursor (privadas) devem ser, no mínimo:

- avançarKPosições( K )
- retrocederKPosições ( K )
- irParaPrimeiro()
- irParaUltimo()

Outras:

- `boolean` Vazia()
- `boolean` Cheia()
- `boolean` contém(chave)
- `boolean` posiçãoDe(chave)

### Implementação

O desenvolvimento consiste em implementar as funções descritas da maneira mais simples, porém correta.

Não foi elaborado nenhum esquema de como funcionaria cada função, porém o seu funcionamento está descrito no `Docstring Comments` presente abaixo da declaração de cada método em `List.py`. O objeto `Item`, presente em `Item.py` é apenas uma modificação do já previamente implementado `Item`, que possui apontamentos para o próximo e anterior valor da lista.

Não foi preciso o desenvolvimento de um objeto `Ponteiro` pois somente com manipulação de "ponteiros" já foi possível a implementação.

Para ter uma ideia do funcionamento dessa lista duplamente encadeada, o arquivo `__main__.py` possui uma demonstração simples de como seria utilizada em contexto real o objeto `Lista` + `Item`.
