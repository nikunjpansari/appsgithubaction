import pytest
from src.numerical_operations import (
    add, sub, mul, div, floor_div, mod, power,
    bit_and, bit_or, bit_xor, bit_not, lshift, rshift
)


def test_add():
    assert add(2, 3) == 5
    assert add(-1, 1) == 0


def test_sub():
    assert sub(5, 3) == 2
    assert sub(4, 3) == 1
    assert sub(3, 3) == 0
    assert sub(2, 3) == -1

def test_mul():
    assert mul(3, 4) == 12
    assert mul(-2, 5) == -10

def test_div():
    assert div(10, 2) == 5
    with pytest.raises(ValueError):
        div(1, 0)

def test_floor_div():
    assert floor_div(7, 3) == 2
    assert floor_div(-7, 3) == -3
    with pytest.raises(ValueError):
        floor_div(1, 0)

def test_mod():
    assert mod(10, 3) == 1
    with pytest.raises(ValueError):
        mod(1, 0)

def test_power():
    assert power(2, 3) == 8
    assert power(5, 0) == 1

def test_bitwise_and_or_xor():
    assert bit_and(0b1100, 0b1010) == 0b1000
    assert bit_or(0b1100, 0b1010) == 0b1110
    assert bit_xor(0b1100, 0b1010) == 0b0110

def test_bit_not():
    # ~x == -x-1
    assert bit_not(0) == -1
    assert bit_not(1) == -2

def test_shifts():
    assert lshift(1, 3) == 8
    assert rshift(8, 2) == 2
