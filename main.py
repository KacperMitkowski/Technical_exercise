def add_expressions(*first_args):
    def helper(*second_args):
        elements = first_args + second_args

        if not all(isinstance(arg, int) for arg in elements):
            raise TypeError("not int arg in function")
        if len(first_args) == 0 or len(second_args) == 0:
            raise TypeError("no arguments given to function")

        result_dict = {}
        for el in elements:
            if elements.count(el) > 1:
                result_dict[el] = el * 2
            else:
                result_dict[el] = el
        return result_dict

    return helper


try:
    outcome = add_expressions(1, 1, 2)(2, 4)
    result = ""
    for key, value in outcome.items():
        result += f'{value}X**{key} + '
    result += '0'

    print(result)
except TypeError as e:
    print(e)
