import pytest 
from app import calculate

def testcapitalcase():
    f = 4
    g = 5 
    resultat = calculate(f,g)
    assert (resultat == f+g)
