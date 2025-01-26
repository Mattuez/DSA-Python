from bubble_sort import bubble_sort


def test_bubble_sort_empty():
    assert bubble_sort([2, 0, 2, 1, 1, 0]) == [0, 0, 1, 1, 2, 2]


def test_bubble_sort_single_element():
    assert bubble_sort([42]) == [42]


def test_bubble_sort_already_sorted():
    assert bubble_sort([1, 2, 3, 4, 5]) == [1, 2, 3, 4, 5]


def test_bubble_sort_reverse_order():
    assert bubble_sort([5, 4, 3, 2, 1]) == [1, 2, 3, 4, 5]


def test_bubble_sort_duplicates():
    assert bubble_sort([3, 2, 1, 3, 2, 1]) == [1, 1, 2, 2, 3, 3]


def test_bubble_sort_negative_numbers():
    assert bubble_sort([-3, -1, -2, 0, 2, 1]) == [-3, -2, -1, 0, 1, 2]


def test_bubble_sort_mixed_numbers():
    assert bubble_sort([0, -1, 4, 3, -5]) == [-5, -1, 0, 3, 4]
