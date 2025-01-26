from linear_search import linear_search

def test_linear_search():
    assert linear_search([1, 2, 3, 4, 5], 1) is True
    assert linear_search([1, 2, 3, 4, 5], 10) is False