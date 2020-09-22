from Item import Item

class Stack:

    def __init__(self, max: int = 0):
        self.max = max
        self.itemCnt = 0
        self.item = None

    def full(self):
        return self.itemCnt == self.max

    def pop(self):
        if isinstance(self.item, Item):
            tmpItem = self.item

            self.itemCnt -= 1
            self.item = tmpItem.link

            return tmpItem.value
        else:
            raise(BaseException("Cannot pop an empty stack"))

    def push(self, value):
        if self.full():
            raise(BaseException("Cannot push into a full stack"))

        tmpItem = Item(value, self.item)

        self.itemCnt += 1
        self.item = tmpItem

        return self

    def top(self):
        if not isinstance(self.item, Item):
            raise(BaseException("Cannot top an empty stack"))
        
        return self.item.value
