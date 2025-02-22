class DoubleLinkedListNode:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.previous = None
    def __str__(self):
        return self.data

class DoubleLinkedList:
    def __init__(self):
        self.head = None
        self.tail = None
        self._size = 0
    
    def append(self, elem):
        if self.tail:
            node = DoubleLinkedListNode(elem)
            self.tail.next = node
            node.previous = self.tail
            self.tail = node
            self._size += 1
        else:
            node = DoubleLinkedListNode(elem)
            self.head = node
            self.tail = node
            self._size += 1
    
    def __len__(self):
        return self._size
    
    def __getitem__(self, index):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            return pointer.data
        else:
            raise IndexError("list index out of range")
        
    def __setitem__(self, index, elem):
        pointer = self.head
        for i in range(index):
            if pointer:
                pointer = pointer.next
            else:
                raise IndexError("list index out of range")
        if pointer:
            pointer.data = elem
        else:
            raise IndexError("list index out of range")

    def index(self, elem):
        pointer = self.head
        i = 0
        while(pointer):
            if pointer.data == elem:
                return i
            pointer = pointer.next
            i += 1
        raise ValueError(f"{elem} is not in list")

    def insert(self, index, elem):
            pointer = self.head
            for i in range(index - 1):
                if pointer:
                    pointer = pointer.next
                else:
                    raise IndexError("list index out of range")
            node = DoubleLinkedListNode(elem)
            node.next = pointer.next
            pointer.next = node

    def shift(self):
        if self.head is None:
            raise IndexError("list is empty")
        self.head = self.head.next
        self._size -= 1

    def unshift(self, elem):
        node = DoubleLinkedListNode(elem)
        node.next = self.head
        self.head = node