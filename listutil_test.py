import unittest
from listutil import unique


class ListUntilTest(unittest.TestCase):
    def test_one_item(self):
        self.assertEqual(["a"], unique(["a"]))
        self.assertEqual([[1]], unique([[1, ]]))
        self.assertEqual(["b"], unique(["b", "b", "b"]))

    def test_more_items(self):
        self.assertEqual(["a", "b", "c"], unique(["a", "b", "b", "c"]))
        self.assertEqual([1, 2, 3], unique([1, 1, 2, 3]))

    def test_empty_list(self):
        self.assertFalse(unique([]))

    def test_list_in_list(self):
        self.assertEqual(3, len(unique([1, 2, 2, [3, 2, 1]])))
        self.assertEqual(1, len(unique([[], []])))

    def test_is_list(self):
        with self.assertRaises(ValueError):
            type(unique("1234"))
        with self.assertRaises(ValueError):
            type(unique(1234))
        with self.assertRaises(ValueError):
            type(unique((1, 2)))
        with self.assertRaises(ValueError):
            type(unique({"hi": "dict"}))

    def test_extreme_list(self):
        self.assertEqual(["b", "a", "c"], unique(
            ['b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a',
             'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a',
             'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a',
             'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a',
             'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a',
             'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a', 'b', 'a', 'a', 'c', 'b', 'a',
             'b', 'a', 'a', 'c', 'b', 'a']))


if __name__ == '__main__':
    unittest.main()
