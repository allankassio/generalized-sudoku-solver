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
