from sympy import pretty_print as pp
from sympy.abc import a, b, n, x


def add_expressions(*first_args):
    def helper(*second_args):
        elements = list(first_args) + list(second_args)
        d = {}
        for el in elements:
            if elements.count(el) > 1:
                d[el] = el * 2
            else:
                d[el] = el
        return d

    return helper


outcome = add_expressions(1, 2, 8)(2, 3)

for key, value in outcome.items():
    expr = (x) ** key
    pp(int(value) * expr)
