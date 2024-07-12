import unittest

class TestSetOperations(unittest.TestCase):

    def test_set_add(self):
        my_set = {1, 2, 3}
        my_set.add(4)
        self.assertIn(4, my_set)

    def test_set_remove(self):
        my_set = {1, 2, 3}
        my_set.remove(2)
        self.assertNotIn(2, my_set)

    def test_set_intersection(self):
        set1 = {1, 2, 3, 4}
        set2 = {3, 4, 5, 6}
        intersection = set1.intersection(set2)
        self.assertEqual(intersection, {3, 4})

    def test_set_union(self):
        set1 = {1, 2, 3}
        set2 = {3, 4, 5}
        union = set1.union(set2)
        self.assertEqual(union, {1, 2, 3, 4, 5})

if __name__ == '__main__':
    unittest.main()
