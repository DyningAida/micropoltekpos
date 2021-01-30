import sys
sys.path.insert(1, 'src/')
from app import index

def test_index():
    assert index() == "Hello, world!"
