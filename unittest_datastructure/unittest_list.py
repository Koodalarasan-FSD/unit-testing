import unittest

class TestListOperations(unittest.TestCase):

    def test_list_append(self):
        my_list = []
        my_list.append(1)
        self.assertEqual(my_list, [1])

    def test_list_insert(self):
        my_list = [1, 2, 3]
        my_list.insert(1, 4)
        self.assertEqual(my_list, [1, 4, 2, 3])

    def test_list_remove(self):
        my_list = [1, 2, 3]
        my_list.remove(2)
        self.assertEqual(my_list, [1, 3])

    def test_list_index(self):
        my_list = [1, 2, 3]
        self.assertEqual(my_list.index(2), 1)

    def test_list_pop(self):
        my_list = [1, 2, 3]
        popped = my_list.pop()
        self.assertEqual(popped, 3)
        self.assertEqual(my_list, [1, 2])

if __name__ == '__main__':
    unittest.main()
