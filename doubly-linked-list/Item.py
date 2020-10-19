class Item:

    def __init__(self, value: any, previous = None, next = None):
        self.value = value

        if previous is not None:
            self.previous = previous
        else:
            self.previous = None

        if next is not None:
            self.next = next
        else:
            self.next = None
    
    def set_previous(self, item = None):
        self.previous = item
    
    def get_previous(self):
        return self.previous

    def set_next(self, item = None):
        self.next = item
    
    def get_next(self):
        return self.next
