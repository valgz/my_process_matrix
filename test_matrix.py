from process_any_matrix import *
import pytest


def test_process_matrix():

    m1 = [[2, 0, 1], [0, 1, 1], [1, 0, 1]]
    m2 = [[3, 2.5, 0, 1], [2, 3, 1, 9]]
    m3 = [[4, 3], [0, 5], [2, 7], [1, 0]]
    m4 = []
    #m5 = [[3, 0, 2], [], [2, 0]]
    #m6 = [[2, 1], None, [8, 9]]
    #m7 = [[3, 4], [True, 0], []]
    #m8 = [[3.9, True, 0], ['0', 1, 0], ['k', None, 7]]

    assert process_matrix(m1) == [[0.67, 1.0, 0.67], [1.0, 0.4, 1], [0.33, 0.75, 0.67]]
    assert process_matrix(m2) == [[2.5, 2.12, 1.12, 3.33], [2.67, 2.12, 3.25, 3.67]]
    assert process_matrix(m3) == [[2.33, 4.0], [2.75, 3.75], [2.5, 3.5], [1.0, 2.67]]
    assert process_matrix(m4) == []
    #assert process_matrix(m5) == None
    #assert process_matrix(m6) == None
    #assert process_matrix(m7) == None
    #assert process_matrix(m8) == None




