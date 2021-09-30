from aver import *
import sys
sys.path.append(".")

def test_average():
    assert average([1,2,3]) ==2

def test_hap():
    assert hap(1,1) == 3
