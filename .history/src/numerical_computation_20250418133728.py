def add(a, b):
    return a + b


def sub(a, b):
    return a - b


def mul(a, b):
    return a * b


def div(a, b):
    if b == 0:
        raise ValueError("Cannot divide by zero")
    return a / b


def floor_div(a, b):
    if b == 0:
        raise ValueError("Cannot floor-divide by zero")
    return a // b


def mod(a, b):
    if b == 0:
        raise ValueError("Cannot mod by zero")
    return a % b


def power(a, b):
    return a ** b

# Bitwise operations (on integers)
def bit_and(a, b):
    return a & b

def bit_or(a, b):
    return a | b

def bit_xor(a, b):
    return a ^ b

def bit_not(a):
    return ~a

def lshift(a, n):
    return a << n

def rshift(a, n):
    return a >> n