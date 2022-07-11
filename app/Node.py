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
