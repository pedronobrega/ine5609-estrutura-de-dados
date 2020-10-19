from Item import Item

class List:

  def __init__(self, size: int = 0):
    self.size = size
    self.itemCnt = 0
    self.pointer: Item = None

  # Pointer Methods

  def goAheadPositions(self, number: int):
    i = 0
    current: Item = self.accessActual()
    if self.isEmpty():
      raise('Empty List')
  
    while current is not None and i != number:
      current = current.next
      i += 1
    
    self.pointer = current

  def goBackPositions(self, number: int):
    i = 0
    current: Item = self.accessActual()
    if self.isEmpty():
      raise('Empty List')
    
    while current is not None and i != 0:
      current = current.next
      i -= 1
    
    self.pointer = current

  def goToFirst(self):
    first = None
    current: Item = self.pointer
    while current is not None:
      first = current
      current = current.previous
    
    self.pointer = first

  def goToLast(self):
    last = None
    current: Item = self.pointer
    while current is not None:
      last = current
      current = current.next

    self.pointer = last
  
  def isFirst(self):
    return self.pointer.previous is None
  
  def isLast(self):
    return self.pointer.next is None

  # Support Methods

  def isEmpty(self):
    return self.pointer is None
  
  def isFull(self):
    return self.size == self.itemCnt

  def doesHaveValue(self, value):
    self.goToFirst()
    current = self.accessActual()
    haveValue = False

    if current is None:
      return False

    if current.value == value:
      return True

    while haveValue is False and current is not None:
      current = current.next
      haveValue = current.value if current is not None else False
  
    return haveValue

  def positionOf(self, value):
    item = None

  # Public Methods

  def accessActual(self):
    return self.pointer