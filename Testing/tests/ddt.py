from main import *
from samples import a
import pytest

@pytest.mark.parametrize(
    "d, expected",
    [
        ({1: 2, 3: 4, 5: 6}, {(1,): 2, (3,): 4, (5,): 6}),
        (1, {(): 1}),
        ({1: {1: {1: 1}}, 2: {2: 2}}, {(1, 1, 1): 1, (2, 2): 2}),
    ]
)
def test_flatten(d, expected):
    assert flatten(d) == expected

@pytest.mark.parametrize(
    "a, path, expected",
    [
        (a, (), a),
        (a, ('a',), a['a']),
        (a, ('e', 0), a['e'][0]),
        (a, ('e', []), [{'x': 1, 'y': 1}, {'x': 2, 'y': 2}, {'x': 3, 'y': 3}, {'x': 4, 'y': 4}]),
        (a, ('z',), KeyError),
    ]
)
def test_deep_traverse(a, path, expected):
    if isinstance(expected, type) and issubclass(expected, Exception):
        with pytest.raises(expected):
            deep_traverse(a, path)
    else:
        assert deep_traverse(a, path) == expected

@pytest.mark.parametrize(
    "i1, i2, element_mapping, element_filter, expected",
    [
        (
            {'a': 1, 'b': 2, 'c': 3},
            {'b': 10, 'c': 20, 'd': 30},
            None,
            None,
            {'a': (1, None), 'b': (2, 10), 'c': (3, 20), 'd': (None, 30)}
        ),
        (
            [1, 2, 3],
            [10, 20, 30],
            None,
            None,
            {0: (1, 10), 1: (2, 20), 2: (3, 30)}
        ),
        (
            10,
            20,
            lambda a, b: (b, a),
            None,
            (20, 10)
        ),
        (
            5,
            5,
            None,
            lambda a, b: a > b,
            None
        ),
    ]
)
def test_per_itempair(i1, i2, element_mapping, element_filter, expected):
    assert per_itempair(i1, i2, element_mapping, element_filter) == expected

@pytest.mark.parametrize(
    "d1, d2, expected",
    [
        (
            {'a': 1, 'b': 2, 'c': 3},
            {'b': 10, 'c': 20, 'd': 30},
            {'a': (1, None), 'b': (2, 10), 'c': (3, 20), 'd': (None, 30)}
        ),
        ({}, {}, {}),
    ]
)
def test_dictsum(d1, d2, expected):
    assert dictsum(d1, d2) == expected

@pytest.mark.parametrize(
    "l1, l2, expected",
    [
        (
            [1, 2, 3],
            [10, 20, 30],
            {0: (1, 10), 1: (2, 20), 2: (3, 30)}
        ),
        ([], [], {}),
    ]
)
def test_listsum(l1, l2, expected):
    assert listsum(l1, l2) == expected
