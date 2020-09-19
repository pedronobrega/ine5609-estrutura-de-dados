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

    def test_push_should_raise_exception_when_full(self):
        newObject = Stack(1)
        newObject.push(3)

        self.assertRaises(BaseException, newObject.push)

    def test_top_should_return_value(self):
        item = Item(3)
        newObject = Stack()

        newObject.item = item

        self.assertEqual(3, newObject.top())

    def test_top_should_raise_exception_when_empty(self):
        newObject = Stack()

        self.assertRaises(BaseException, newObject.top)

    def test_stack(self):
        newObject = Stack(3)
        newObject.push(1)
        newObject.push('ABC')
        newObject.push(2.0)

        self.assertRaises(BaseException, newObject.push)

        self.assertEqual(2.0, newObject.pop())
        self.assertEqual('ABC', newObject.pop())
        self.assertEqual(1, newObject.pop())

        self.assertRaises(BaseException, newObject.pop)
        self.assertRaises(BaseException, newObject.top)

if __name__ == '__main__':
    unittest.main()