class Item:

    def __init__(self, value: any, link = None):
        self.__value = value,
        self.__link = link

    @property
    def value(self):
        return self.__value

    def link(self):
        return self.__link
