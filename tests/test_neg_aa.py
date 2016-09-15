import pytest
import tdd_test_driven_dev as tdd

def test_n_neg():
    """ """
    assert tdd.n_neg('D') == 1
    assert tdd.n_neg('E') == 1
    assert tdd.n_neg('') == 0
    assert tdd.n_neg('ACKWTTAE') == 1
    assert tdd.n_neg('aaaaaadaaa') == 1
    assert tdd.n_neg('DEEDEE') == 6
#    assert tdd.n_neg('*') == 0

    pytest.raises(RuntimeError, "tdd.n_neg('Z')")


    return None
