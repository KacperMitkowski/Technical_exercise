import unittest

from main import add_expressions


class TestAddingExpressions(unittest.TestCase):
    def test_if_add_expressions_returns_dict_type(self):
        self.assertIsInstance(add_expressions(1, 2, 8)(2, 3), dict)

    def check_if_giving_not_int_to_func_raises_type_error(self):
        self.assertRaises(TypeError, add_expressions(1, 2, 'test')(2, 4, 9))
        self.assertRaises(TypeError, add_expressions(1, 2)(2, 4, 9, 'test'))
        self.assertRaises(TypeError, add_expressions(1, 2)(2, 4, 9, None))
        self.assertRaises(TypeError, add_expressions(1, 2, None)(2, 4, 9, ))

    def check_if_giving_no_args_to_func_raises_type_error(self):
        self.assertRaises(TypeError, add_expressions()())
        self.assertRaises(TypeError, add_expressions(1, 2, 3)())
        self.assertRaises(TypeError, add_expressions()(1, 2, 3))

    def test_if_add_expressions_returns_correct_values(self):
        self.assertDictEqual(add_expressions(1, 2, 8)(2, 4), {1: 1, 2: 4, 8: 8, 4: 4})
        self.assertDictEqual(add_expressions(1, 1, 2)(2, 4), {1: 2, 2: 4, 4: 4})
        self.assertDictEqual(add_expressions(1, 1, 2)(0, 4), {1: 2, 2: 2, 0: 0, 4: 4})

    def test_if_keys_or_values_in_result_dict_are_int(self):
        for key, value in add_expressions(1, 2, 8)(2, 3).items():
            self.assertIsInstance(key, int)
            self.assertIsInstance(value, int)
