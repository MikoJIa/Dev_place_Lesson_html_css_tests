import unittest


class Calculater:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def get_sum(self):
        return self.x + self.y

    def get_diff(self):
        return self.x - self.y


class TestCalculater(unittest.TestCase):

    def test_sum(self):
        calculater = Calculater(8, 2)
        self.assertEqual(calculater.get_sum(), 10, 'The sum is wrong')

    def test_diff(self):
        calculater = Calculater(8, 2)
        self.assertEqual(calculater.get_diff(), 6, 'The differance is wrong')



