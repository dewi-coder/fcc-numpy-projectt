import unittest
from mean_var_std import calculate

class UnitTests(unittest.TestCase):
    def test_calculate(self):
        actual = calculate([0,1,2,3,4,5,6,7,8])
        expected = {
          'mean': [[3.0, 4.0, 5.0], [1.0, 4.0, 7.0], 4.0],
          'variance': [[6.0, 6.0, 6.0], [0.6666666666666666]*3, 6.666666666666667],
          'standard deviation': [[2.449489742783178]*3, [0.816496580927726]*3, 2.581988897471611],
          'max': [[6, 7, 8], [2, 5, 8], 8],
          'min': [[0, 1, 2], [0, 3, 6], 0],
          'sum': [[9, 12, 15], [3, 12, 21], 36]
        }
        for key in expected:
            for i in range(3):
                if isinstance(expected[key][i], list):
                    for j in range(len(expected[key][i])):
                        self.assertAlmostEqual(actual[key][i][j], expected[key][i][j], places=5)
                else:
                    self.assertAlmostEqual(actual[key][i], expected[key][i], places=5)

    def test_calculate_with_invalid_input(self):
        with self.assertRaises(ValueError) as context:
            calculate([1, 2, 3])
        self.assertEqual(str(context.exception), "List must contain nine numbers.")
