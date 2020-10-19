from List import List
from Item import Item

if __name__ == "__main__":
  lista: List = List(3)

  # This will throw an exception
  # lista.go_ahead_positions(3)

  # This will print None
  print(lista.access_actual())

  # This will print True
  print(lista.is_empty())

  # This will print False
  print(lista.is_full())

  item1 = Item(123)
  lista.insert_at_the_start(item1)
  # This will print 123
  print(lista.access_actual().value)

  item2 = Item(456)
  lista.insert_at_the_end(item2)
  # This will print 456
  print(lista.go_to_last().value)
  