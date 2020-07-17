def add_expressions(*first_args):
    def helper(*second_args):
        elements = list(first_args) + list(second_args)
        d = {}
        for el in elements:
            if elements.count(el) > 1:
                d[el] = el * 2
            else:
                d[el] = el
        yield d

    return helper

result = ""
for el in add_expressions(1, 2, 8)(2, 3):
    for key, value in el.items():

        result += f'{value}X**{key} + '
    result += '0'

print(result)


