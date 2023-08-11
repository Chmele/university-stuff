from unittest import TestCase
from main import *
from samples import a


class TestUtil(TestCase):
    def test_flatten(self):
        d = {
            1: 2, 
            3: 4, 
            5: 6
        }
        f = {
            (1,): 2, 
            (3,): 4, 
            (5,): 6
        }
        self.assertEqual(flatten(d), f)
        self.assertEqual(flatten(1), {(): 1})
        d = {
            1: {
                1: {1: 1}
            }, 
            2: {
                2: 2
            }
        }
        self.assertEqual(flatten(d), {(1, 1, 1): 1, (2, 2): 2})
    
    def test_deep_traverse(self):
        test = self.assertEqual
        test(deep_traverse(a, ()), a)
        test(deep_traverse(a, ('a')), a['a'])
        test(deep_traverse(a, ('e', 0)), a['e'][0])
        test(deep_traverse(a, ('e', [])), [{'x': 1, 'y': 1}, {'x': 2, 'y': 2}, {'x': 3, 'y': 3}, {'x': 4, 'y': 4}])
        with self.assertRaises(KeyError):
            deep_traverse(a, ('z'))


class PerItemPairTest(TestCase):
    def test_per_itempair_dict(self):
        i1 = {'a': 1, 'b': 2, 'c': 3}
        i2 = {'b': 10, 'c': 20, 'd': 30}
        expected_result = {'a': (1, None), 'b': (2, 10), 'c': (3, 20), 'd': (None, 30)}
        result = per_itempair(i1, i2)
        self.assertEqual(result, expected_result)

    def test_per_itempair_list(self):
        i1 = [1, 2, 3]
        i2 = [10, 20, 30]
        expected_result = {0: (1, 10), 1: (2, 20), 2: (3, 30)}
        result = per_itempair(i1, i2)
        self.assertEqual(result, expected_result)

    def test_per_itempair_custom_mapping(self):
        i1 = 10
        i2 = 20
        expected_result = (20, 10)
        result = per_itempair(i1, i2, element_mapping=lambda a, b: (b, a))
        self.assertEqual(result, expected_result)

    def test_per_itempair_custom_filter(self):
        i1 = 5
        i2 = 5
        expected_result = None
        result = per_itempair(i1, i2, element_filter=lambda a, b: a > b)
        self.assertEqual(result, expected_result)


class DictSumTest(TestCase):
    def test_dictsum(self):
        d1 = {'a': 1, 'b': 2, 'c': 3}
        d2 = {'b': 10, 'c': 20, 'd': 30}
        expected_result = {'a': (1, None), 'c': (3, 20), 'd': (None, 30), 'b': (2, 10)}
        result = dictsum(d1, d2)
        self.assertEqual(result, expected_result)

    def test_dictsum_empty_dicts(self):
        d1 = {}
        d2 = {}
        expected_result = {}
        result = dictsum(d1, d2)
        self.assertEqual(result, expected_result)

class ListSumTest(TestCase):
    def test_listsum(self):
        l1 = [1, 2, 3]
        l2 = [10, 20, 30]
        expected_result = {0: (1, 10), 1: (2, 20), 2: (3, 30)}
        result = listsum(l1, l2)
        self.assertEqual(result, expected_result)

    def test_listsum_empty_lists(self):
        l1 = []
        l2 = []
        expected_result = {}
        result = listsum(l1, l2)
        self.assertEqual(result, expected_result)

