class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if not self.is_empty():
            return self._items.pop()
        raise IndexError("Pop from empty stack")

    def peek(self):
        if not self.is_empty():
            return self._items[-1]
        raise IndexError("Peek from empty stack")

    def is_empty(self):
        return len(self._items) == 0

    def size(self):
        return len(self._items)
