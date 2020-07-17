import unittest

from main import add_expressions


class TestAddingExpressions(unittest.TestCase):
    def test_if_add_expressions_returns_dict_type(self):
        self.assertIsInstance(add_expressions(1, 2, 8)(2, 3), dict)

    def check_if_giving_not_int_to_func_raises_type_error(self):
        self.assertRaises(TypeError, add_expressions(1, 2, "test")(2, 4, 9))
        self.assertRaises(TypeError, add_expressions(1, 2)(2, 4, 9, "test"))
        self.assertRaises(TypeError, add_expressions(1, 2)(2, 4, 9, None))
        self.assertRaises(TypeError, add_expressions(1, 2, None)(2, 4, 9,))

    def test_if_add_expressions_returns_correct_values(self):
        print(add_expressions(1, 2, 8)(2, 4))