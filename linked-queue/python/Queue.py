from Item import Item

class Queue:

    def __init__(self, max: int = 0):
        self.__max = max
        self.__itemCnt = 0
        self.__item: Item = None

    def __item__(self, item: Item = None):
        self.__item = item

    def full(self):
        return self.__itemCnt == self.__max

    def enqueue(self, item: Item):
        if self.full():
            self.dequeue()
        
        actual = self.__item
        last = None
        while actual is not None:
            last = actual
            actual = actual.link
        
        self.__itemCnt += 1
        last.link(item)

    def dequeue(self):
        tmp = self.__item
        self.__item = tmp.link
        return tmp