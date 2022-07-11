---
abstract: |
  This paper presents an implementation for solving generalized Sudoku
  puzzles using backtracking and Dancing Links algorithms. Two
  algorithms were implemented, one using the backtracking technique and
  the other using the Dancing Links technique. The algorithms were
  tested on Sudokus of different sizes (9x9, 16x16 and 25x25) and the
  execution time was measured. The results show that the Dancing Links
  algorithm is more efficient than the backtracking algorithm for
  solving generalized Sudoku puzzles.
address: |
  Programa de Pós-Graduação Doutorado em Ciência da Computação\
  Associação UFMA-UFPI (DCCMAPI)\
  Universidade Federal do Manhão (FMA) -- São Luís, MA -- Brazil
author:
- Allan K. B. S. da Cruz, João D. de S. Almeida
bibliography:
- references.bib
title: "Resolvendo Sudokus Generalizados através de algoritmos de
  *backtracking* e de *Dancing Links*"
---

::: {.resumo}
Este trabalho apresenta uma implementação da resolução de sudokus
generalizados através de algoritmos de backtracking e Dancing Links.
Foram implementados dois algoritmos, um utilizando a técnica de
backtracking e outro utilizando a técnica de Dancing Links. Os
algoritmos foram testados em diferentes tamanhos de sudoku (9x9, 16x16 e
25x25) e o tempo de execução foi medido. Os resultados mostraram que o
algoritmo de Dancing Links é mais eficiente que o algoritmo de
backtracking para a resolução de sudokus generalizados.
:::

# Introdução

O Sudoku é um jogo de lógica que consiste em um quadro 9x9 dividido em
subquadros 3x3, no qual cada subquadro contém os dígitos de 1 a 9 sem
repetição e cada linha e coluna do quadro também contém os dígitos de 1
a 9 sem repetição [@felgenhauer_mathematics_2006]. O objetivo do jogo é
preencher os quadros com os dígitos de 1 a 9 de tal forma que cada
dígito apareça apenas uma vez em cada linha, coluna e subquadro. O
tabuleiro inicia com alguns espaços previamente preenchidos (geralmete
com inteiros de 1 a n). A
Figura [1](#fig:gridsudoku){reference-type="ref"
reference="fig:gridsudoku"} mostra uma intância do Sudoku 9x9 e uma
possível solução.

[Grid Sudoku 9x9 com solução. Adaptado de:
[@dreamstime_sudoku_2018]]{.image}

A história dos quebra-cabeças de Sudoku provavelmente tem suas raízes no
conceito matemático de quadrados latinos [@mckay_number_2005]. Eles são
um tipo de quadrado mágico, uma tabela quadrada contendo números
naturais, tal que a soma dos números em cada linha, coluna, diagonal e
quadrado mágico principal é a mesma. A
Figura [2](#fig:quadradolatino){reference-type="ref"
reference="fig:quadradolatino"} mostra um exemplo de um quadrado latino
de ordem 4.

[Quadrado latino de ordem 4. Adaptado de:
[@nogueira_quadrados_2015]]{.image}

Os quadrados latinos foram introduzidos pela primeira vez pelo
matemático suíço Leonhard Euler em 1782. Em 1892, Euler apresentou o
problema de determinar se existe um quadrado latino de ordem 9
[@cota_euler_2011]. Esse problema permaneceu sem resposta até 1915,
quando o matemático estadunidense Sam Loyd publicou um quadrado latino
de ordem 9 em sua revista americana de matemática, Mathematical Puzzles
[@costa_matematica_2014].

No entanto, Loyd afirmou que esse quadrado latino de ordem 9 era um
problema de \"brinquedo\", e não uma demonstração de um teorema
matemático. O tabuleiro de Sudoku que conhecemos hoje, no entanto, é uma
prova de um teorema matemático. Em 1979, o matemático japonês Tetsuya
Nishio e seus colegas demonstraram que existe um número infinito de
tabuleiros de Sudoku que satisfazem as propriedades do jogo
[@tsao_evolutionary_2019].

Assim pode-se dizer que o Sudoku é um jogo relativamente novo. O nome do
jogo é uma contração da frase em japonês suuji wa dokushin ni kagiru,
que significa \"os números devem estar sozinhos\". O jogo ganhou
popularidade nos Estados Unidos nos anos 2000 e, desde então, tem sido
um dos jogos de lógica mais populares do mundo [@maia_jogos_2012].

## Sudoku Generalizado

Um sudoku generalizado é um sudoku em que as dimensões da grade de jogo
são ajustáveis [@haynes_analysis_2008]. Isso significa que, em vez de
uma grade 9x9, um sudoku generalizado pode ser uma grade de qualquer
tamanho, como 16x16 (Figura [3](#fig:16x16sudoku){reference-type="ref"
reference="fig:16x16sudoku"}), 25x25 ou 36x36. Além disso, as regras
podem ser ajustadas para permitir que os jogadores usem qualquer número
de 1 a 9, ou até mesmo letras ou símbolos diferentes.

[Grid Sudoku 16x16. Adaptado de: [@knupfer_suitability_2014]]{.image}

O Sudoku generalizado é um problema de otimização NP-completo, o que
significa que, em princípio, não existe um algoritmo que possa resolver
o problema de forma eficiente para todos os possíveis casos
[@maji_sudoku_2014]. Isto é devido à natureza de exponencial do
problema, uma vez que aumentando o tamanho da grade do Sudoku,
aumenta-se exponencialmente o número de possíveis soluções.

Um problema NP-difícil é um problema para o qual não existe um algoritmo
de polynomial para resolvê-lo. Isso significa que, se um problema é
NP-difícil, então não existe um algoritmo que possa resolvê-lo em tempo
polinomial [@rai_polynomial_2018]. No entanto, existem algoritmos que
podem resolver problemas NP-difíceis em tempo subpolinomial, mas esses
algoritmos são considerados ineficientes [@yildirim_study_2008]. Para
tentar aproximar-se do resultado ideal são utilizadas heurísticas para
prover soluções.

Uma heurística é uma técnica que busca uma solução aproximada para um
problema de otimização NP-completo, de forma a encontrar uma solução que
seja \"suficientemente boa\". Não existe uma heurística única que seja
capaz de resolver todos os problemas de Sudoku, uma vez que cada
problema é único e pode requerer uma abordagem diferente
[@takano_o_2015].

Uma heurística comum para o Sudoku é a de tentar preencher as células
vazias com os valores que restam, de forma a minimizar o número de
valores que faltam para completar a grade [@dittrich_solving_2010].
Outra heurística é a de procurar as células que têm o menor número de
valores possíveis e tentar preenchê-las com esses valores
[@takano_o_2015].

Existem muitas outras heurísticas que podem ser usadas para resolver
problemas de Sudoku, e é importante experimentar várias delas para
encontrar aquela que melhor se adapta ao problema em questão.

# Algoritmos de Resolução de Sudoku Generalizado

Existem vários algoritmos diferentes que podem ser usados para resolver
um Sudoku Generalizado, mas a maioria dos algoritmos segue os mesmos
princípios básicos. O primeiro passo é determinar o tamanho do quadrado
e, em seguida, preencher as linhas e colunas com os números de 1 a N. Em
seguida, é necessário determinar os blocos e, finalmente, preenchê-los
com os números restantes.

Uma vez que o quadrado estiver completamente preenchido, é possível
verificar se a solução é correta, comparando-a com as regras do Sudoku
Generalizado. Se a solução estiver correta, é possível parar o
algoritmo. Se a solução não estiver correta, é necessário verificar se
há algum erro na solução e, se houver, corrigi-lo.

No entanto a solução para um Sudoku se enquandra como um problema da
cobertura exata. Que é um problema de otimização combinatória que trata
de encontrar um subconjunto de um determinado conjunto tal que os
elementos do subconjunto cubram todos os elementos do conjunto dado, e
dois elementos do subconjunto não cubram o mesmo elemento do dado
conjunto. definir [@kapanowski_python_2010]. O problema de cobertura
exata é um exemplo de problema de satisfação de restrição. Na maioria
dos casos, quando são instâncias de solução possíveis, são resolvidos
por algoritmos recursivos com backtracking. Dentre os algoritmos que
resolvem o sudoku e se encaixam na cobertura exata podemos destacar os
seguintes:

-   **Minimum Remaining Values:** defende que e mais viável selecionar
    variáveis com menos possibilidades de valores [@abuluaih_fog_2018].
    Ou seja, para o Sudoku, significa selecionar a celula com menos
    candidatos de inserção para toda vez que for necessário procurar uma
    nova celula.

-   **Forward Checking:** propõe o término quando finaliza a busca caso
    alguma variável ainda não testada não tenha valores dentro de seu
    domínio [@simonis_sudoku_2005]. Para o caso do Sudoku, toda vez que
    o Backtracking encontrar uma célula em que não será possível inserir
    mais nenhum valor, a busca é finalizada e testada para um próximo
    estado [@skiena_algorithm_2008].

-   **Manipulação de Bits:** técnica utilizada para representação das
    estruturas de dados do Sudoku e manipulação das unidades (linha,
    coluna e bloco) com consulta em tempo constante [@takano_o_2015].
    Implementa o modelo teorico de coloração em hipergrafos,
    aplicando-se a ideia de que as unidades são hiperarestas, e assim o
    acesso para verificação de um dígito nas unidades durante a execução
    do método é O(1). Para que a Manipulação de Bits ocorra é necessário
    que se guarde todos os dígitos pre-preenchidos do tabuleiro do
    Sudoku em vetores. Cada dígito do tabuleiro é representado por um
    algarismo de um numero presente no vetor. A verificação é a remoção
    de dígitos e feita através dos vetores criados.

-   **Constraint Propagation:** uma técnica que remove valores de um
    domínio de variaveis da qual não iráo participar de nenhuma solução
    [@russell_artificial_2010]. Enquanto o algoritmo for executado
    atraves da busca em profundidade, a técnica irá remover os
    candidatos do tabuleiro da qual seriam impossíveis de ser inseridas.

-   **Dancing Links:** técnica proposta por Donald Knuth
    [@knuth_dancing_2000], também conhecida como DLX, para implementar
    de forma eficiente seu algoritmo X. O algoritmo X e um tipo de
    backtracking com podas, uma busca em profundidade recursiva
    nao-determinística, que encontra todas as soluões para realizar a
    cobertura exata do problema.

Assim neste trabalho foi escolhido implementar o algoritmo de Dancing
Links e paralelamente, a título de comparação de performance, um
algoritmo trivial baseado backtracking.

## Backtracking

Como todos os outros problemas de Backtracking, o Sudoku pode ser
resolvido passo a passo, atribuindo números às células vazias. Antes de
atribuir um número, devemos verificar se podemos atribuir. Verifica-se
se o mesmo número não está presente na linha atual, coluna atual e
subgrade atual. Depois de verificar a segurança, devmos atribuir um
número e verificar recursivamente se essa atribuição leva a uma solução
ou não. Se a atribuição não levar a uma solução, devemos tentar o
próximo número para a célula vazia atual. E se nenhum dos números (1 a
9) levar a uma solução, devemos retornar falso e imprimir que não existe
solução (nesse caso, provavelmente há um problema com a grade original
gerada).

É necessário criar uma função que verifique, após atribuir o índice
atual, se a grade se torna insegura ou não. Devemos manter um hashmap
para uma linha, coluna e caixas. Se algum número tiver uma frequência
maior que 1 no hashmap, retornamos falso, caso contrário, retornamos
verdadeiro (o hashmap pode ser evitado usando loops).

Em resumo, o algoritmo segue essa ordem:

1.  Crie uma função recursiva que recebe uma grade.

2.  Verifique se há algum local não atribuído.

3.  Se presente, atribua um número de 1 a $n^{2}$, verifique se atribuir
    o número ao índice atual torna a grade insegura ou não.

4.  Se for segura, chame recursivamente a função para todos os casos
    seguros de 0 a $n^{2}$.

5.  Se qualquer chamada recursiva retornar true, finaliza o loop e
    retornar true.

6.  Se nenhuma chamada recursiva retornar true, então retorne false.

7.  Se não houver local não atribuído, retorne true.

### Análise de Complexidade do Backtraking

Complexidade de tempo: $O((n^{2})^{(n*n)})$. Para cada índice não
atribuído, existem $n^{2}$. opções possíveis, então a complexidade de
tempo é $O((n^{2})^{(n*n)})$. A complexidade de tempo permanece a mesma,
mas haverá algumas podas iniciais, de modo que o tempo gasto será muito
menor do que o algoritmo ingênuo, mas a complexidade de tempo do limite
superior permanece a mesma.

Complexidade espacial: $O(n*n)$, pois para armazenar a saída é
necessária uma estrutura do tipo matriz.

## Dancing Links

Programas para resolver o Sudoku, geralmente caem no problema da
cobertura total ou cobertura exata. Esse tipo de problema pode ser
resolvido com o algoritmo conhecido como "Algoritmo X"
[@knuth_dancing_2000].

Dada uma coleção S de subconjuntos do conjunto X, uma cobertura exata é
o subconjunto S\* de S tal que cada elemento de X contido é exatamente
um subconjunto de S\* [@knuth_dancing_2000]. Deve satisfazer as
seguintes duas condições:

-   A interseção de quaisquer dois subconjuntos em S\* deve estar vazia.
    Ou seja, cada elemento de X deve estar contido em no máximo um
    subconjunto de S\*

-   A união de todos os subconjuntos em S\* é X. Isso significa que a
    união deve conter todos os elementos do conjunto X. Então podemos
    dizer que S\* cobre X.

Exemplo (representação padrão):

Seja $$\textup{S = \{ A, B, C, D, E, F \}}$$ $$e$$
$$\textup{X = \{1, 2, 3, 4, 5, 6, 7\}}$$ tal que:

A = {1, 4, 7}, B = {1, 4}, C = {4, 5, 7}, D = {3, 5, 6}, E = {2, 3, 6
7}, F = {2, 7}.

Então S\* = {B, D, F} é uma cobertura exata, porque cada elemento em X
está contido exatamente uma vez nos subconjuntos {B, D, F} . Se unirmos
subconjuntos, obteremos todos os elementos de X:

$$B \bigcup D \bigcup F = \{ 1,2,3,4,5,6,7\}$$

O problema da cobertura exata é um problema de decisão para determinar
se a cobertura exata existe ou não. É considerado um problema
NP-Completo. O problema pode ser representado na forma de uma matriz
onde a linha representa os subconjuntos de S e as colunas representam o
elemento de X.

### Algoritmo X

O Algoritmo X foi proposto visando poder encontrar todas as soluções
para o problema de cobertura exata. O Algoritmo X pode ser implementado
eficientemente pela técnica de Dancing Links (ou links dançantes),
proposta pelo mesmo autor, chamada DLX [@knuth_dancing_2000].

É um algoritimo recursivo, primeiro em profundidade, e um algoritmo que
usa o conceito de backtraking. É de natureza não determinística, o que
significa que, para a mesma entrada, pode exibir comportamentos
diferentes em uma execução diferente.

A seguir está o pseudocódigo para o Algoritmo X:

1.  Se a matriz A não tiver colunas, a solução parcial atual é uma
    solução válida; terminar com sucesso.

2.  Caso contrário, escolha uma coluna c (deterministicamente).

3.  Escolha uma linha r tal que A\[r\] = 1 (não deterministicamente).

4.  Inclua a linha r na solução parcial.

5.  Para cada coluna j tal que A\[r\]\[j\] = 1,

    1.  para cada linha i tal que A\[i\]\[j\] = 1,

        1.  exclua a linha i da matriz A.

    2.  exclua a coluna j da matriz A.

6.  Repita este algoritmo recursivamente na matriz reduzida A.

7.  Escolha não determinística de r significa, o algoritmo copia a si
    mesmo no subalgoritmo. Cada subalgoritmo herda a matriz original A,
    mas a reduz em relação ao r escolhido (veremos isso em breve no
    exemplo)

O subalgoritmo forma uma árvore de busca com o problema original na raiz
e cada nível k tem um subalgoritmo que corresponde às linhas escolhidas
no nível anterior (assim como o espaço de busca) [@knuth_dancing_2000].

Se a coluna escolhida C for totalmente zero, então não há subalgoritmos
e o processo terminou sem sucesso. [@knuth_dancing_2000] sugere que
devemos escolher a coluna com o número mínimo de 1s. Se não sobrar
nenhuma coluna, então sabemos que encontramos nossa solução.

A técnica do Dancing Links baseia-se na ideia de lista encadeada
duplamente circular. Conforme discutido por [@knuth_dancing_2000],
transforma-se o problema de cobertura exata em forma de matriz de 0 e 1.
Aqui cada "1" na matriz é representado por um nó de lista encadeada e
toda a matriz é transformada em uma malha de nós conectados de 4 vias.
Cada nó contém os seguintes campos:

-   Ponteiro para o nó à esquerda dele

-   Ponteiro para o nó direito a ele

-   Ponteiro para o nó acima dele

-   Ponteiro para o nó abaixo dele

-   Ponteiro para listar o nó do cabeçalho ao qual pertence

Cada linha da matriz é, portanto, uma lista circular vinculada entre si
com ponteiros para a esquerda e para a direita e cada coluna da matriz
também será uma lista circular vinculada a cada uma acima e abaixo com
os ponteiros para cima e para baixo. Cada lista de colunas também inclui
um nó especial chamado "nó de cabeçalho de lista". Este nó de cabeçalho
é como um nó simples, mas tem poucos campos extras:

-   Código da coluna

-   Contagem de nós na coluna atual

Podemos ter dois tipos diferentes de nós, um para as colunas que possui
o \"atributo tamanho\" e um para os nós \"dançantes\", que possui o
atributo que identifica o \"cabeçalho da coluna\".

# Conclusão

Como dito anteriormente as soluções escolhidas foram a de Backtracking e
de Dancing Links. Cada um desses algoritmos foi implementado como uma
classe separada. Adicionamente foram implementadas classes para o
Iterador, para o Nó, para representar a Matriz do Sudoku, para gerar o
sudoku a partir dos datasets e para validação do sudoku. Os códigos do
sistema estão disponíveis no Anexo deste trabalho e no repositório
GitHub: <https://github.com/allankassio/generalized-sudoku-solver>.

## Base de dados utilizada

A base de dados utilizada consiste em quatro aqruivos CSV que modelam e
representam os puzzles do soduko como linhas únicas. Cada coluna é
composta por dois dígitos (permitindo assim casas maiores do que 9).
Para cada tamanho N do rank representado, os arquivos possuem $2(N^2)$
dígitos por linha.

Para tabuleiros de 9x9 a base de dados possui 3000 entradas. Para 16x16,
25x25 e 36x36 são 10 entradas para cada um. Já 49x49 possui 6 entradas,
enquanto 64x64 tem 5 entradas e 81x81 tem apenas 1 entrada. A
Figura [4](#fig:base){reference-type="ref" reference="fig:base"} mostra
um exemplo de 3 entradas de dados do tipo 9x9.

[Exemplo de base de dados utilizada.]{.image}

## Exemplos de saídas

As saídas são compostas do número de iterações necessárias para resolver
o sudoku, o tempo levado para a resolução e se aquela resposta é válida.
A Figura [5](#fig:saida){reference-type="ref" reference="fig:saida"}
mostra um exemplo de saídas no console.

[Exemplo de saída no console para entradas com n=5.]{.image}

## Comparação dos algoritmos

Para comparar o algoritmo de backtracking com o de Dancing Links foram
utilizados os seguintes critérios: comparação da média dos 10 primeiros
resultados para matrizes 9x9, 16x16 e 25x25 tanto tem termo de iterações
quanto em termo de tempo médio. Ambos algoritmos utilizaram a mesma base
de dados como entrada. Na Figura [6](#fig:comp3){reference-type="ref"
reference="fig:comp3"} podemos vemos a comparação para n=3. Na
Figura [7](#fig:comp4){reference-type="ref" reference="fig:comp4"}
podemos vemos a comparação para n=4. Na
Figura [8](#fig:comp5){reference-type="ref" reference="fig:comp5"}
podemos vemos a comparação para n=5.

[Comparação de desempenho com n=3.]{.image}

O algoritmo de Backtracking apresenta um crescimento exponencial muito
rápido a medida que aumentamos o valor de n. Em contrapartida, o Dancing
Links, mesmo também apresentando crescimento exponencial, apresenta para
a grande maioria dos casos tempos abaixo de 1 segundo.

[Comparação de desempenho com n=4.]{.image}

[Comparação de desempenho com n=5.]{.image}

Com isso é possível perceber que Dancing Links pode ser mais eficiente
que backtracking para resolver o sudoku, dependendo da implementação,
dependendo do tamanho do sudoku e da entropia da entrada. Dancing links
consegue resolver sudoku de forma eficiente porque ao contrário de
backtracking, dancing links não precisa fazer muitas buscas caso existam
várias soluções. Isso é possível pois ele utiliza listas encadeadas
circulares para representar os dados.

# ANEXOS {#anexos .unnumbered}

``` {.python language="Python" caption="main.py"}
import csv
import time

from app.SudokuBackTrackingSolver import SudokuBackTrackingSolver
from app.SudokuExactCoverSolver import SudokuExactCoverSolver
from app.SudokuGenerator import SudokuGenerator
from app.SudokuValidator import SudokuValidator


def run_exact_cover_solver():
    for n in range(3, 6):
        print(f'n={n}')
        main_solver(
            solver=SudokuExactCoverSolver,
            n=n,
            write_to_csv=True
        )


def run_backtracking_solver():
    for n in range(3, 6):
        print(f'n={n}')
        main_solver(
            solver=SudokuBackTrackingSolver,
            n=n,
            write_to_csv=True
        )


def main_solver(solver, n, num_puzzles=None, write_to_csv=False):

    print(f'{solver.__name__}')
    results = [('num_updates', 'time_taken', 'is_valid')]

    sudoku_generator = SudokuGenerator(n)
    sudoku_matrices = sudoku_generator.generate_puzzles(num_puzzles)

    for sudoku_matrix in sudoku_matrices:
        num_updates, time_taken = solve_puzzle(solver, sudoku_matrix)
        sudoku_validator = SudokuValidator(sudoku_matrix)
        is_valid = sudoku_validator.validate()
        print((n, num_updates, time_taken, is_valid))
        results.append((num_updates, time_taken, is_valid))

    if write_to_csv:
        write_data_to_csv(results, f'output/sudoku_rank_{n}_{solver.__name__}.csv')
    else:
        [print(r) for r in results]

    return results


def solve_puzzle(solver, sudoku_matrix):
    s = solver(sudoku_matrix)

    start = time.time()
    s.solve()
    end = time.time()
    num_updates = s.get_num_updates()
    return num_updates, end - start


def write_data_to_csv(results, csv_file):
    with open(csv_file, 'w') as csv_file:
        writer = csv.writer(csv_file)
        [writer.writerow([r for r in result]) for result in results]


def main():
    # Rodar esses dois métodos vai permitir executar
    # todos os testes dos ranks 3 até 5 (9x9, 16x16 e 25x25)
    # ===========================================================
    # run_exact_cover_solver()
    # run_backtracking_solver()

    # Rodar dessa forma permite definir qual dataset vai
    # ser utilizado apenas mudando o N, desde que n>=3 e n<=9.
    # Para cada valor de n, o tamanho da matriz será de n**2
    # ===========================================================
    # main_solver(solver=SudokuBackTrackingSolver, n=4, write_to_csv=True)
    main_solver(solver=SudokuExactCoverSolver, n=5, write_to_csv=True)
    main_solver(solver=SudokuBackTrackingSolver, n=4, write_to_csv=True)
    main_solver(solver=SudokuBackTrackingSolver, n=5, write_to_csv=True)

if __name__ == "__main__":
    main()
```

``` {.python language="Python" caption="Node.py"}
class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.row_id = None
        self.column_id = None


class DancingNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.column_header = None


class ColumnNode(Node):
    def __init__(self, value):
        super().__init__(value)
        self.size = 0
```

``` {.python language="Python" caption="Iterator.py"}
class LeftIterable(object):

    def __init__(self, node):
        self.node = node
        self.original_node = node

    def __iter__(self):
        return self

    def __next__(self):
        self.node = self.node.left

        if self.node == self.original_node:
            raise StopIteration

        return self.node


class RightIterable(object):

    def __init__(self, node):
        self.node = node
        self.original_node = node

    def __iter__(self):
        return self

    def __next__(self):
        self.node = self.node.right

        if self.node == self.original_node:
            raise StopIteration

        return self.node


class UpIterable(object):

    def __init__(self, node):
        self.node = node
        self.original_node = node

    def __iter__(self):
        return self

    def __next__(self):
        self.node = self.node.up

        if self.node == self.original_node:
            raise StopIteration

        return self.node


class DownIterable(object):

    def __init__(self, node):
        self.node = node
        self.original_node = node

    def __iter__(self):
        return self

    def __next__(self):
        self.node = self.node.down

        if self.node == self.original_node:
            raise StopIteration

        return self.node
```

``` {.python language="Python" caption="SudokuMatrix.py"}
from tabulate import tabulate


class SudokuMatrix:

    def __init__(self, n):
        self.n = n  # classificação (rank)
        self.k = 0  # número de pistas (números preenchidos)
        self.sudoku_matrix = [[0 for _ in range(n ** 2)] for _ in range(n ** 2)]
        self.EMPTY_CELL = 0

    def __str__(self):
        return tabulate(self.get_rows(), tablefmt="fancy_grid")

    def get(self, row, column):
        return self.sudoku_matrix[row][column]

    def get_rows(self):
        return self.sudoku_matrix

    def get_row(self, row):
        return self.sudoku_matrix[row]

    def get_columns(self):
        return [*zip(*self.sudoku_matrix)]

    def get_column(self, column):
        return self.get_columns()[column]

    def get_boxes(self):
        indices = [(x % self.n, int(x / self.n)) for x in range(self.n ** 2)]
        boxes = [[self.sudoku_matrix[x * self.n + xx][y * self.n + yy] for xx, yy in indices] for x, y in indices]
        return boxes

    def get_box(self, row, column):
        box_index = self.get_box_index(row, column)
        return self.get_boxes()[box_index]

    def get_box_index(self, row, column):
        indices = [(x % self.n, int(x / self.n)) for x in range(self.n ** 2)]

        xx = row % self.n
        yy = column % self.n

        x = (row - xx) / self.n
        y = (column - yy) / self.n

        return indices.index((x, y))

    def get_rank(self):
        return self.n

    def get_num_clues(self):
        return self.k

    def get_empty_cells(self):
        empty_cells = []

        for row in range(self.n ** 2):
            for column in range(self.n ** 2):
                if self.is_empty_cell(row, column):
                    empty_cells.append((row, column))

        return empty_cells

    def has_empty_cells(self):
        for row in range(self.n ** 2):
            for column in range(self.n ** 2):
                if self.is_empty_cell(row, column):
                    return True

        return False

    def is_empty_cell(self, row, column):
        return self.get(row, column) == self.EMPTY_CELL

    def set(self, row, column, value):
        self.sudoku_matrix[row][column] = value

        if value != self.EMPTY_CELL:
            self.increment_num_clues()

    def set_if_valid(self, row, column, value):
        if self.is_valid(row, column, value):
            self.set(row, column, value)
            return True

        return False

    def make_cell_empty(self, row, column):
        self.set(row, column, self.EMPTY_CELL)

    def increment_num_clues(self):
        self.k += 1

    def is_valid(self, row, column, value):
        if value in self.get_row(row):
            return False

        if value in self.get_column(column):
            return False

        if value in self.get_box(row, column):
            return False

        return True
```

``` {.python language="Python" caption="SudokuValidator.py"}
from app.SudokuMatrix import SudokuMatrix


def contains_duplicates(arr):
    if len(set(arr)) != len(arr):
        return True

    return False


class SudokuValidator:

    # :type sudoku_matrix: SudokuMatrix
    def __init__(self, sudoku_matrix):

        self.sudoku_matrix = sudoku_matrix

    def validate(self):

        fully_filled = not self.sudoku_matrix.has_empty_cells()
        validated_rows = self._validate_rows()
        validated_columns = self._validate_columns()
        validated_boxes = self._validate_box()

        return fully_filled and validated_rows and validated_columns and validated_boxes

    def _validate_rows(self):
        for row in self.sudoku_matrix.get_rows():
            if contains_duplicates(row):
                return False

        return True

    def _validate_columns(self):
        for column in self.sudoku_matrix.get_columns():
            if contains_duplicates(column):
                return False

        return True

    def _validate_box(self):
        for box in self.sudoku_matrix.get_boxes():
            if contains_duplicates(box):
                return False

        return True
```

``` {.python language="Python" caption="SudokuGenerator.py"}
import csv

from app.SudokuMatrix import SudokuMatrix


class SudokuGenerator:

    def __init__(self, n):
        self.n = n
        self.csv_file = f'datasets/sudoku_rank_{self.n}.csv'

    def generate_puzzles(self, num_puzzles=None):
        puzzles = self._read_sudoku_csv(num_puzzles)
        return [self._convert_string_to_matrix(puzzle) for puzzle in puzzles]

    def generate_puzzle_from_id(self, i):
        with open(self.csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            sudoku_puzzle = list(csv_reader)[i][0]

        return [self._convert_string_to_matrix(sudoku_puzzle)]

    def _read_sudoku_csv(self, num_puzzles=None):
        sudoku_puzzles = []
        with open(self.csv_file) as csv_file:
            csv_reader = csv.reader(csv_file, delimiter=',')
            next(csv_reader, None)  # pula o cabeçalho

            for i, row in enumerate(csv_reader):
                if num_puzzles and len(sudoku_puzzles) == num_puzzles:
                    break

                sudoku_puzzles.append(row[0])

        return sudoku_puzzles

    def _convert_string_to_matrix(self, sudoku_string):
        sudoku_matrix = SudokuMatrix(self.n)

        c = 0
        for i in range(self.n ** 2):
            for j in range(self.n ** 2):
                if sudoku_string[c] == '.':
                    sudoku_matrix.set(i, j, 0)
                else:
                    sudoku_matrix.set(i, j, int(sudoku_string[c:c + 2]))
                c += 2

        return sudoku_matrix
```

``` {.python language="Python" caption="DancingLinks.py"}
from app.Node import DancingNode, ColumnNode


class DancingLinks:
    def __init__(self, matrix):
        self.matrix = matrix
        self._pad_matrix()

    # Atualiza a matriz de entrada adicionando cabeçalhos de coluna
    # e matriz de preenchimento com 0s para mantê-lo um quadrado perfeito
    def _pad_matrix(self):
        for row in self.matrix:
            row.insert(0, 0)

        column_headers = []
        for j in range(len(self.matrix[0])):
            if j == 0:
                # inserir nó de cabeçalho
                column_headers.append('H')
            else:
                # inserir cabeçalhos de coluna
                column_headers.append(f'C{j}')
        self.matrix.insert(0, column_headers)

    # Método usado para conectar todos os nós usando listas duplamente vinculadas
    def create_dancing_links(self):
        nodes = self._create_nodes()
        self._create_links_between_nodes(nodes)

    # Converte todos os cabeçalhos de coluna e células com 1s em nós
    def _create_nodes(self):
        nodes = []
        for i in range(len(self.matrix)):
            for j in range(len(self.matrix[i])):
                value = self.matrix[i][j]
                # nada a ser feito quando é 0
                if value == 0:
                    continue
                node = None
                # converter todos os 1 para DancingNode
                if value == 1:
                    node = DancingNode(value)
                # converter todos os cabeçalhos de coluna para ColumnNode
                if value != 1 and value != 0:
                    node = ColumnNode(value)
                node.row_id = i
                node.column_id = j
                nodes.append(node)
                self.matrix[i][j] = node

        return nodes

    # Cria um link entre nós que estão conectados à esquerda,
    # direita, para cima e para baixo.
    # Além disso, cada DancingNode é referenciado a um ColumnNode
    def _create_links_between_nodes(self, nodes):

        for node in nodes:
            node.left = self._get_left(node.row_id, node.column_id)
            node.right = self._get_right(node.row_id, node.column_id)
            # o nó de cabeçalho não precisa de links para cima ou para baixo
            if node.value != 'H':
                node.up = self._get_up(node.row_id, node.column_id)
                node.down = self._get_down(node.row_id, node.column_id)
            # criar referência ao cabeçalho da coluna
            if node.value == 1:
                node.column_header = self._get_column_header(node.column_id)
                node.column_header.size += 1

    # Retorna o nó à esquerda do nó em (linha, coluna)
    def _get_left(self, row, column):
        j = (column - 1) % len(self.matrix[row])
        while self.matrix[row][j] == 0:
            j = (j - 1) % len(self.matrix[row])
        return self.matrix[row][j]

    # Retorna o nó à direita do nó em (linha, coluna)
    def _get_right(self, row, column):
        j = (column + 1) % len(self.matrix[row])
        while self.matrix[row][j] == 0:
            j = (j + 1) % len(self.matrix[row])
        return self.matrix[row][j]

    # Retorna o nó acima do nó em (linha, coluna)
    def _get_up(self, row, column):
        i = (row - 1) % len(self.matrix)
        while self.matrix[i][column] == 0:
            i = (i - 1) % len(self.matrix)
        return self.matrix[i][column]

    # Retorna o nó abaixo do nó em (linha, coluna)
    def _get_down(self, row, column):
        i = (row + 1) % len(self.matrix)
        while self.matrix[i][column] == 0:
            i = (i + 1) % len(self.matrix)
        return self.matrix[i][column]

    # Retorna o cabeçalho da coluna do nó na coluna
    def _get_column_header(self, column):

        return self.matrix[0][column]
```

``` {.python language="Python" caption="ExactCoverSolver.py"}
import sys

from app.Iterator import DownIterable, RightIterable, LeftIterable, UpIterable
from app.DancingLinks import DancingLinks


class ExactCoverSolver:

    def __init__(self, exact_cover_matrix):
        self.exact_cover_matrix = exact_cover_matrix
        DancingLinks(exact_cover_matrix).create_dancing_links()
        self.header = self.exact_cover_matrix[0][0]
        self.num_updates = 0
        self.answer = []

    # Busca do Algoritmo X
    def search(self, k, o):

        if self.header.right == self.header:
            self.answer.append(o.copy())
            return

        c = self._choose_column()
        self._cover(c)

        for r in DownIterable(c):
            o[k] = r

            for j in RightIterable(r):
                self._cover(j.column_header)

            self.search(k + 1, o)

            r = o.pop(k, None)
            c = r.column_header

            for j in LeftIterable(r):
                self._uncover(j.column_header)

        self._uncover(c)
        return

    def get_num_updates(self):
        return self.num_updates

    def get_answer(self):
        return self.answer

    # Retorna a coluna com o menor número de 1s.
    def _choose_column(self):

        min_size = sys.maxsize
        column_selected = None

        for c in RightIterable(self.header):
            if c.size < min_size:
                min_size = c.size
                column_selected = c

        return column_selected

    def _cover(self, c):
        self._unlinkLR(c)

        for i in DownIterable(c):
            for j in RightIterable(i):
                self._unlinkUD(j)
                j.column_header.size -= 1

    def _uncover(self, c):
        for i in UpIterable(c):
            for j in LeftIterable(i):
                j.column_header.size += 1
                self._relinkUD(j)

        self._relinkLR(c)

    def _unlinkUD(self, x):
        x.down.up = x.up
        x.up.down = x.down
        self.num_updates += 1

    def _relinkUD(self, x):
        x.down.up = x
        x.up.down = x
        self.num_updates += 1

    def _unlinkLR(self, x):
        x.right.left = x.left
        x.left.right = x.right
        self.num_updates += 1

    def _relinkLR(self, x):
        x.right.left = x
        x.left.right = x
        self.num_updates += 1
```

``` {.python language="Python" caption="SudokuExactCoverSolver.py"}
from app.ExactCoverSolver import ExactCoverSolver


class SudokuExactCoverSolver:

    # :type sudoku_matrix: SudokuMatrix
    def __init__(self, sudoku_matrix):

        self.sudoku_matrix = sudoku_matrix
        self.n = sudoku_matrix.get_rank()
        self.exact_cover_matrix, self.possibilities = self._create_exact_cover_matrix()
        self.exact_cover_solver = ExactCoverSolver(self.exact_cover_matrix)

    def solve(self):
        self.exact_cover_solver.search(k=0, o=dict())
        solutions = self.exact_cover_solver.get_answer()

        for solution in solutions[0].values():
            row, column, value = self.possibilities[solution.row_id - 1]
            if self.sudoku_matrix.is_empty_cell(row, column):
                self.sudoku_matrix.set(row, column, value)

    def get_num_updates(self):
        return self.exact_cover_solver.get_num_updates()

    def _create_exact_cover_matrix(self):
        possibilities = self._create_possibilities()
        constraints = self._create_constraints()
        exact_cover_matrix = []

        for possibility in possibilities:
            m = []
            for constraint in constraints:
                m.append(self._handle_possibility_constraint_combination(possibility, constraint))
            exact_cover_matrix.append(m)

        return exact_cover_matrix, possibilities

    def _create_possibilities(self):
        possibilities = []

        for row in range(self.n ** 2):
            for column in range(self.n ** 2):
                if self.sudoku_matrix.is_empty_cell(row, column):
                    for i in range(1, self.n ** 2 + 1):
                        if self.sudoku_matrix.is_valid(row, column, i):
                            possibilities.append((row, column, i))
                else:
                    possibilities.append((row, column, self.sudoku_matrix.get(row, column)))

        return possibilities

    def _create_constraints(self):
        constraints = []

        # restrição de linha-coluna
        for row in range(self.n ** 2):
            for column in range(self.n ** 2):
                constraints.append(('rc', row, column))

        # restrição de número de linha
        for row in range(self.n ** 2):
            for number in range(1, self.n ** 2 + 1):
                constraints.append(('rn', row, number))

        # restrição de número de coluna
        for column in range(self.n ** 2):
            for number in range(1, self.n ** 2 + 1):
                constraints.append(('cn', column, number))

        # restrição de número de caixa
        for box in range(self.n ** 2):
            for number in range(1, self.n ** 2 + 1):
                constraints.append(('bn', box, number))

        return constraints

    def _handle_possibility_constraint_combination(self, possibility, constraint):
        row, column, value = possibility
        constraint_type, x, y = constraint

        if constraint_type == 'rc':
            return 1 if row == x and column == y else 0

        if constraint_type == 'rn':
            return 1 if row == x and value == y else 0

        if constraint_type == 'cn':
            return 1 if column == x and value == y else 0

        if constraint_type == 'bn':
            box_index = self.sudoku_matrix.get_box_index(row, column)
            return 1 if box_index == x and value == y else 0
```

``` {.python language="Python" caption="SudokuBackTrackingSolver.py"}
from app.SudokuMatrix import SudokuMatrix


class SudokuBackTrackingSolver:

    # :tipo sudoku_matrix: SudokuMatrix
    def __init__(self, sudoku_matrix):

        self.sudoku_matrix = sudoku_matrix
        self.n = sudoku_matrix.get_rank()
        self.num_backtracks = 0  # contador para medir a performance do algoritmo

    def solve(self):

        if not self.sudoku_matrix.has_empty_cells():
            return True

        current_row, current_column = self.sudoku_matrix.get_empty_cells()[0]

        for i in range(1, self.n ** 2 + 1):

            if self.sudoku_matrix.set_if_valid(current_row, current_column, i):
                if self.solve():
                    return True

                # Caso chegue nessa parte, faz o backtracking
                self.sudoku_matrix.make_cell_empty(current_row, current_column)
                self.num_backtracks += 1

        return False

    def get_num_updates(self):
        return self.num_backtracks
```
