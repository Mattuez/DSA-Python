import pytest

from binary_search import binary_search

@pytest.mark.parametrize("arr, number, expected", [
    ([1, 2, 3, 4, 5, 6], 3, True),   # Caso feliz: número está no meio da lista
    ([1, 2, 3, 4, 5], 1, True),   # Número no início da lista
    ([1, 2, 3, 4, 5], 5, True),   # Número no final da lista
    ([1, 2, 3, 4, 5], 6, False),  # Número não está na lista
    ([1, 2, 3, 4, 5], 0, False),  # Número abaixo do menor valor
    ([], 1, False),               # Lista vazia
    ([10], 10, True),             # Lista com um único elemento (valor encontrado)
    ([10], 5, False),             # Lista com um único elemento (valor não encontrado)
    ([1, 3, 5, 7, 9], 4, False),  # Número entre dois valores na lista
    ([2, 4, 6, 8, 10], 8, True),  # Lista apenas com números pares
])
def test_binary_search(arr, number, expected):
    assert binary_search(arr, number) == expected
