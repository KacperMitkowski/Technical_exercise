def add_expressions(*first_args):
    def helper(*second_args):
        elements = first_args + second_args

        if not all(isinstance(arg, int) for arg in elements):
            raise TypeError("not int arg in function")

        d = {}
        for el in elements:
            if elements.count(el) > 1:
                d[el] = el * 2
            else:
                d[el] = el
        return d

    return helper

# try:
#     outcome = add_expressions(1, 2, 8)(2, 4)
#     result = ""
#     for key, value in outcome.items():
#         result += f'{value}X**{key} + '
#     result += '0'
#
#     print(result)
# except TypeError as e:
#     print(e)
