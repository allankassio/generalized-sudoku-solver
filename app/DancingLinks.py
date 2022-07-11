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
