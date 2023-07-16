"""
A simple script to show how to use Python's built-in pdb debugger.
"""


def sum_two(a, b):
    return a + b


def multiply_two(a, b):
    return a * b


def cast_string(a):
    return str(a)


def sum_strings(a, b):
    return a + b


if __name__ == "__main__":
    ai = 5
    bi = 10
    ci = sum_two(ai, bi)
    di = multiply_two(ai, bi)
    breakpoint()

    cs = cast_string(ci)
    ds = cast_string(di)
    es = sum_strings(cs, ds)

    print(es)
