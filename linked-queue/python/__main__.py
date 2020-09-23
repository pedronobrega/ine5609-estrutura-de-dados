import unittest
from Queue import Queue
from Item import Item

class TestQueue(unittest.TestCase):
    
    def test_init(self):
        newObject = Queue()

        self.assertIsInstance(newObject, Queue)
        self.assertEqual(0, newObject.max)
        self.assertEqual(0, newObject.itemCnt)
        self.assertIsNone(newObject.item)

    def test_full_should_be_full(self):
        newObject = Queue()
        newObject.max = 3
        newObject.itemCnt = 3

        self.assertTrue(newObject.full())
    
    def test_full_should_not_be_full(self):
        newObject = Queue()
        newObject.max = 3
        newObject.itemCnt = 2

        self.assertFalse(newObject.full())

    def test_dequeue_should_return_value(self):
        item = Item(3)
        newObject = Queue()

        newObject.item = item

        self.assertEqual(item.value, newObject.dequeue())

    def test_dequeue_should_raise_exception_when_empty(self):
        newObject = Queue()

        self.assertRaises(BaseException, newObject.dequeue)

    def test_enqueue_should_enqueue_value(self):
        newObject = Queue(1)
        expectedResult = 'abc'

        newObject.enqueue(expectedResult)

        self.assertEqual(expectedResult, newObject.item.value)

    def test_enqueue_should_enqueue_values(self):
        newObject = Queue(3)
        
        newObject.enqueue(1)
        newObject.enqueue(2)
        newObject.enqueue(3)

        self.assertEqual(3, newObject.itemCnt)

    def test_enqueue_should_enqueue_when_full(self):
        newObject = Queue(1)
        newObject.enqueue(3)
        newObject.enqueue(4)

        self.assertEqual(4, newObject.item.value)
        self.assertEqual(1, newObject.itemCnt)

    def test_top_should_return_value(self):
        item = Item(3)
        newObject = Queue()

        newObject.item = item

        self.assertEqual(3, newObject.top())

    def test_top_should_raise_exception_when_empty(self):
        newObject = Queue()

        self.assertRaises(BaseException, newObject.top)

    def test_Queue(self):
        newObject = (Queue(3)).enqueue(1).enqueue('ABC').enqueue(2.0)

        self.assertEqual(1, newObject.dequeue())
        self.assertEqual('ABC', newObject.dequeue())
        self.assertEqual(2.0, newObject.dequeue())

        self.assertRaises(BaseException, newObject.dequeue)
        self.assertRaises(BaseException, newObject.top)

if __name__ == '__main__':
    unittest.main()