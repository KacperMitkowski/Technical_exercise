def main():
    """
    :param -
    :return: -

    main function for displaying sum of expressions
    it handles errors exception as well
    """
    try:
        outcome = add_expressions(1, 1, 2)(2, 4)
        result = ''
        for key, value in outcome.items():
            result += f'{value}X**{key} + '
        result += '0'

        print(result)
    except TypeError as e:
        print(e)


def add_expressions(*first_args):
    """
    :param first_args: tuple
    :return: wrapper: func

    Function gets different number of arguments and returns inner function with different number of args as well
    """

    def wrapper(*second_args):
        """
        :param second_args: tuple
        :return: result: dict

        Function gets different number of arguments
        returns dict where key is exponent and value is coefficient
        """
        elements = first_args + second_args

        if not all(isinstance(arg, int) for arg in elements):
            raise TypeError('not int arg in function')
        if len(first_args) == 0 or len(second_args) == 0:
            raise TypeError('no arguments given to function')

        result = {}
        for el in elements:
            if elements.count(el) > 1:
                result[el] = el * 2
            else:
                result[el] = el
        return result

    return wrapper


if __name__ == '__main__':
    main()
