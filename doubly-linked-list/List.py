from Item import Item

class List:

  def __init__(self, size: int = 0):
    self.size = size
    self.itemCnt = 0
    self.pointer: Item = None

  # Pointer Methods

  def go_ahead_positions(self, number: int):
    i = 0
    current: Item = self.access_actual()
    if self.is_empty():
      raise(BaseException('Empty List'))
  
    while current is not None and i != number:
      current = current.get_next()
      i += 1
    
    self.pointer = current

  def go_back_positions(self, number: int):
    i = number
    current: Item = self.access_actual()
    if self.is_empty():
      raise(BaseException('Empty List'))
    
    while current is not None and i != 0:
      current = current.get_next()
      i -= 1
    
    self.pointer = current

  def go_to_first(self):
    first = None
    current: Item = self.access_actual()

    if current is None:
      raise(BaseException('Empty List'))

    elif not self.is_first():
      while current is not None:
        first = current
        current = current.get_previous()
      
      self.pointer = first

  def go_to_last(self):
    last = None
    current: Item = self.access_actual()

    if current is None:
      raise(BaseException('Empty List'))
    
    elif not self.is_last():
      while current is not None:
        last = current
        current = current.get_next()

      self.pointer = last
  
  def is_first(self):
    return self.pointer.get_previous() is None
  
  def is_last(self):
    return self.pointer.get_next() is None

  # Support Methods

  def is_empty(self):
    return self.pointer is None
  
  def is_full(self):
    return self.size == self.itemCnt

  def does_have_value(self, value):
    self.go_to_first()
    current = self.access_actual()
    haveValue = False

    if current is None:
      return False

    if current.value == value:
      return True

    while haveValue is False and current is not None:
      current = current.get_next()
      haveValue = current.value if current is not None else False
  
    return haveValue

  def position_of_value(self, value):
    position = 0
    self.go_to_first()
    while self.pointer.get_next() is not None and self.pointer.value != value:
      position += 1

    return position
    
  # Public Methods

  def access_actual(self):
    return self.pointer
  
  def insert_before_actual(self, new: Item):
    actual = self.access_actual()
    previous = actual.get_previous()
    
    new.set_next(actual)
    new.set_previous(previous)

    actual.set_previous(new)
    previous.set_next(new)
  
  def insert_after_actual(self, new: Item):
    actual = self.access_actual()
    next = actual.get_next()

    new.set_previous(actual)
    new.set_next(next)

    actual.set_next(new)
    next.set_previous(new)
  
  def insert_at_the_end(self, new: Item):
    if self.is_empty():
      self.pointer = new
    elif not self.is_full():
      self.go_to_last()
      actual = self.access_actual()

      new.set_previous(actual)
      actual.set_next(new)
    else:
      raise(BaseException('Cannot insert in a full list'))
  
  def insert_at_the_start(self, new: Item):
    if self.is_empty():
      self.pointer = new
    elif not self.is_full():
      self.go_to_first()
      actual = self.access_actual()

      new.set_next(actual)
      actual.set_previous(new)
    else:
      raise(BaseException('Cannot insert in a full list'))

  def insert_in_position(self, position, new: Item):
    if position > self.size:
      raise(BaseException('Cannot insert'))
    
    self.go_to_first()
    for _ in range(1, position):
      self.pointer = self.pointer.next
    
    self.insert_after_actual(new)

  def remove_actual(self):
    actual = self.access_actual()
    next = actual.get_next()
    previous = actual.get_previous()
    self.go_to_first()

    if next is None:
      previous.set_next()
    if previous is None:
      next.set_previous()
    else:
      next.set_previous(previous)
      previous.set_next(next)

  def remove_first(self):
    self.go_to_first()
    self.remove_actual()
  
  def remove_last(self):
    self.go_to_last()
    self.remove_actual()
  
  def remove_element(self, value):
    position = self.position_of_value(value)
    self.remove_element_from_position(position)
  
  def remove_element_from_position(self, position):
    self.go_to_first()
    self.go_ahead_positions(position)
    self.remove_actual()

  def find_element(self, value):
    position = self.position_of_value(value)
    self.go_to_first()
    self.go_ahead_positions(position)
    
    return self.pointer