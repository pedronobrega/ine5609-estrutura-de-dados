import unittest
from Stack import Stack
from Item import Item

class TestStack(unittest.TestCase):
    
    def test_init(self):
        newObject = Stack()

        self.assertIsInstance(newObject, Stack)
        self.assertEqual(0, newObject.max)
        self.assertEqual(0, newObject.itemCnt)
        self.assertIsNone(newObject.item)

    def test_full_should_be_full(self):
        newObject = Stack()
        newObject.max = 3
        newObject.itemCnt = 3

        self.assertTrue(newObject.full())
    
    def test_full_should_not_be_full(self):
        newObject = Stack()
        newObject.max = 3
        newObject.itemCnt = 2

        self.assertFalse(newObject.full())

    def test_pop_should_return_value(self):
        item = Item(3)
        newObject = Stack()

        newObject.item = item

        self.assertEqual(item.value, newObject.pop())

    def test_pop_should_raise_exception_when_empty(self):
        newObject = Stack()

        self.assertRaises(BaseException, newObject.pop)

    def test_push_should_push_value(self):
        newObject = Stack(1)
        expectedResult = 'abc'

        newObject.push(expectedResult)

        self.assertEqual(expectedResult, newObject.item.value)



if __name__ == '__main__':
    unittest.main()