from crystal_ball_problem import crystal_ball_problem

def test_single_floor():
    """Testa um array com apenas um andar."""
    assert crystal_ball_problem([0]) == -1  # A bola não quebra no único andar.
    assert crystal_ball_problem([1]) == 0  # O único andar quebra a bola.

def test_two_floors():
    """Testa um array com dois andares."""
    assert crystal_ball_problem([0, 0]) == -1  # Nenhum andar quebra.
    assert crystal_ball_problem([0, 1]) == 1  # Primeiro andar não quebra.
    assert crystal_ball_problem([1, 1]) == 0  # Todos os andares quebram a bola.

def test_general_case():
    """Testa casos gerais com arrays maiores."""
    assert crystal_ball_problem([0, 0, 0, 0, 1, 1, 1]) == 4  # Ponto crítico é o índice 4.
    assert crystal_ball_problem([0, 1, 1, 1, 1]) == 1  # Ponto crítico é o índice 1.
    assert crystal_ball_problem([0, 0, 0, 0, 0]) == -1  # Nenhum andar quebra.

def test_large_building():
    """Testa arrays maiores."""
    arr = [0] * 8 + [1]
    assert crystal_ball_problem(arr) == 8  # O ponto crítico é o índice 99.

def test_edge_cases():
    """Testa cenários de borda."""
    assert crystal_ball_problem([1] * 100) == 0  # Todos os andares quebram.
    assert crystal_ball_problem([0] * 100) == -1  # Nenhum andar quebra.