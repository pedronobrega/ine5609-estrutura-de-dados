class Item:

    def __init__(self, value, link: Item = None):
        self.__value = value,
        self.__link = link

    @property
    def link(self):
        return self.__link
    
    @link.setter
    def link(self, item: Item):
        self.__link = item
