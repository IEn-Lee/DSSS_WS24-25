import unittest
from math_quiz import random_integer, random_operator, math_operation


class TestMathGame(unittest.TestCase):

    def test_random_integer(self):
        # Test if random numbers generated are within the specified range
        min_val = 1
        max_val = 10
        for _ in range(1000):  # Test a large number of random values
            rand_num = random_integer(min_val, max_val)
            self.assertTrue(min_val <= rand_num <= max_val)

    def test_random_operator(self):
        # TODO
        # Test if the operator is among the expected options.
        operators = set(['+', '-', '*'])
        for _ in range(1000):
            operator = random_operator()
            self.assertIn(operator, operators)

    def test_math_operation(self):
        # Test if the math_operation function returns the correct problem and answer
        test_cases = [
            (5, 2, '+', '5 + 2', 7),
            (5, 2, '-', '5 - 2', 3),
            (5, 2, '*', '5 * 2', 10),
            (1, 10, '+', '1 + 10', 11),
            (1, 10, '-', '1 - 10', -9),
            (1, 10, '*', '1 * 10', 10),
        ]

        for num1, num2, operator, expected_problem, expected_answer in test_cases:
            # TODO
            problem, answer = math_operation(num1, num2, operator)
            self.assertEqual(problem, expected_problem)
            self.assertEqual(answer, expected_answer)


if __name__ == "__main__":
    unittest.main()
