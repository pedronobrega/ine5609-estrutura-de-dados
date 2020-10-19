# Trabalho de Estrutura de Dados

## Lista duplamente encadeada

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
