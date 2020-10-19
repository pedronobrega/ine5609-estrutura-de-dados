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
  lista.go_to_last()
  # This will print 456
  print(lista.access_actual().value)
  
  item3 = Item(789)
  lista.insert_at_the_start(item3)
  lista.go_to_first()
  # This will print 789
  print(lista.access_actual().value)

  lista.remove_element(456)
  lista.go_to_last()
  # This will print 123
  print(lista.access_actual().value)

  item4 = Item(111)
  lista.insert_in_position(2, item4)
  lista.go_to_last()
  # This will print 111
  print(lista.access_actual().value)