import unittest

class TestDictionaryOperations(unittest.TestCase):

    def test_dict_create(self):
        my_dict = {'a': 1, 'b': 2}
        self.assertEqual(my_dict['a'], 1)
        self.assertEqual(my_dict['b'], 2)

    def test_dict_update(self):
        my_dict = {'a': 1, 'b': 2}
        my_dict['c'] = 3
        self.assertEqual(my_dict['c'], 3)

    def test_dict_delete(self):
        my_dict = {'a': 1, 'b': 2}
        del my_dict['a']
        self.assertNotIn('a', my_dict)
        self.assertEqual(len(my_dict), 1)

    def test_dict_keys(self):
        my_dict = {'a': 1, 'b': 2}
        self.assertEqual(list(my_dict.keys()), ['a', 'b'])

    def test_dict_values(self):
        my_dict = {'a': 1, 'b': 2}
        self.assertEqual(list(my_dict.values()), [1, 2])

if __name__ == '__main__':
    unittest.main()
