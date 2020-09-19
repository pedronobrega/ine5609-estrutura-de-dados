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
        self.item = tmpItem.link
        self.itemCnt -= 1
        return tmpItem.value
            

    def push(self, value):
        if self.full():
            raise(BaseException("Cannot push into a full stack"))
        
        if isinstance(self.item, Item):
            tmpItem = Item(value, self.item)
        else:
            tmpItem = Item(value)

        self.itemCnt += 1
        self.item = tmpItem

    def top(self):
        if not isinstance(self.item, Item):
            raise(BaseException("Cannot top an empty stack"))
        
        return self.item.value
