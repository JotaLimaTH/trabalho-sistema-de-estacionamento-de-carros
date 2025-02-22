class StackNode:
    def __init__(self, data):
        self.data = data
        self.previous = None
    def __str__(self):
        return self.data

class Stack:
    def __init__(self):
        self.last = None
        self.size = 0
    
    def append(self, data):
        node = StackNode(data)
        if self.last is None:
            self.last = node
            self.size += 1
            return node
        pointer = self.last
        self.last = node
        node.previous = pointer
        self.size += 1
        return node

    def remove(self):
        self.last = self.last.previous
        self.size -= 1

    def getStack(self):
        pointer = self.last
        while pointer.previous:
            print(pointer)
            pointer = pointer.previous
    
    def search(self, data):
        pointer = self.last
        while pointer is not None and pointer.data != data:
            pointer = pointer.previous
        if pointer.data == data:
            return pointer