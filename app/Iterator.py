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
