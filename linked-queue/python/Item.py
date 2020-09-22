class Item:

    def __init__(self, value: any, link = None):
        self.value = value

        if link is not None:
            self.link = link
        else:
            self.link = None
