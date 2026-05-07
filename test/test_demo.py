import pytest

@pytest.fixture()
def before_after():
    print('Before test')
    yield
    print('\nAfter test')


def test_demo_1():
    assert 1 == 1
    
