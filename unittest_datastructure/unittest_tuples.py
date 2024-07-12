import unittest

class TestTupleOperations(unittest.TestCase):

    def test_tuple_create(self):
        my_tuple = (1, 2, 3)
        self.assertEqual(my_tuple[0], 1)
        self.assertEqual(my_tuple[1], 2)
        self.assertEqual(my_tuple[2], 3)

    def test_tuple_unpacking(self):
        my_tuple = (1, 2, 3)
        a, b, c = my_tuple
        self.assertEqual(a, 1)
        self.assertEqual(b, 2)
        self.assertEqual(c, 3)

    def test_tuple_immutable(self):
        my_tuple = (1, 2, 3)
        with self.assertRaises(TypeError):
            my_tuple[0] = 4

if __name__ == '__main__':
    unittest.main()
