from Item import Item

class Queue:

    def __init__(self, max: int = 0):
        self.max = max
        self.itemCnt = 0
        self.item: Item = None

    def full(self):
        return self.itemCnt == self.max

    def enqueue(self, item: Item):
        if self.full():
            self.dequeue()
        
        actual = self.item
        last = None
        while actual is not None:
            last = actual
            actual = actual.link

        self.itemCnt += 1
        last.link = item

    def dequeue(self):
        tmp = self.item
        self.item = tmp.link
        return tmp.value
