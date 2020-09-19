from Item import Item

class Stack:

    def __init__(self, max: int = 0):
        self.max = max
        self.itemCnt = 0
        self.item = None

    def full(self):
        return self.itemCnt == self.max

    def pop(self):
        if not isinstance(self.item, Item):
            raise(BaseException("Cannot pop an empty stack"))
        
        tmpItem = self.item
        self.__item__(tmpItem.link)
        self.itemCnt -= 1
        return tmpItem.value
            

    def push(self, value):
        if self.full():
            raise(BaseException("Cannot push into a full stack"))
        
        previousItem = isinstance(self.item, Item) if self.item else None
        tmpItem = Item(value, previousItem)
        self.itemCnt += 1
        self.__item__(tmpItem)
            

    def top(self):
        if not isinstance(self.item, Item):
            raise(BaseException("Cannot top an empty stack"))
        
        return self.item.value

    def __item__(self, item: Item = None):
        self.item = item
