import pytest
from python.questao2a import median

def test_median_odd_list():
    assert median([1, 5, 2, 8, 3]) == 3

def test_median_even_list():
    assert median([1, 6, 2, 8, 3, 10]) == 4.5

def test_median_empty_list():
    with pytest.raises(ValueError, match="A lista não pode estar vazia."):
        median([])

def test_median_non_number_list():
    with pytest.raises(TypeError):
        median([1, "a", 3])