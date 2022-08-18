import pytest
from principal import somar
from principal import subtarir

def test_somar():
    """docstring for test somar"""
    assert somar(2,4) == 6
