from Item import Item

class Queue:

    def __init__(self, max: int = 0):
        self.max = max
        self.itemCnt = 0
        self.item: Item = None

    def full(self):
        return self.itemCnt == self.max

    def enqueue(self, value):
        if self.full():
            self.dequeue()

        actual = self.item
        last = None
        while isinstance(actual, Item):
            last = actual
            actual = actual.link

        if isinstance(last, Item):
            last.link = Item(value)
        else:
            self.item = Item(value)

        self.itemCnt += 1

        return self

    def dequeue(self):
        tmp = self.item
        self.itemCnt -= 1
        self.item = tmp.link
        return tmp.value

    def top(self):
        if isinstance(self.item, Item):
            return self.item.value
        else:
            raise("Cannot top on an empty queue")
