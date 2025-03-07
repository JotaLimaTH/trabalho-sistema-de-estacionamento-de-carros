class QueueNode:
    def __init__(self, data):
        self.data = data
        self.next = None
    def __str__(self):
        return self.data

class Queue:
    def __init__(self):
        self.first = None
        self.size = 0
    
    def append(self, data):
        node = QueueNode(data)
        if self.first is None:
            self.first = node
            self.size += 1
            return node
        pointer = self.first
        while pointer:
            if pointer.next is None:
                pointer.next = node
                self.size +=1
                return node
            pointer = pointer.next

    def remove(self):
        self.first = self.first.next
        self.size -= 1

    def getQueue(self):
        pointer = self.first
        while pointer.next:
            print(pointer.data)
            pointer = pointer.next

    def search(self, data):
        pointer = self.first
        while pointer is not None and pointer.data != data:
            pointer = pointer.next
        if pointer.data == data:
            return pointer