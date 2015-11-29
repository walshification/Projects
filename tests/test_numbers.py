import unittest

from lib.numbers import Numbers


class TestNumbers(unittest.TestCase):
    def setUp(self):
        self.num_fun = Numbers()

    def test_returns_list_of_n_length(self):
        nums = self.num_fun.listonacci_to(42)
        print(nums)
        self.assertEqual(len(nums), 42)

    def test_fibosniper_returns_just_the_nth_fibo_num(self):
        number = self.num_fun.fibosniper(42)
        self.assertEqual(number, 267914296)

    def test_change_returns_change_coins(self):
        coins = self.num_fun.change(1, 2)
        expected = {1.00: 1, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        self.assertEqual(coins, expected)

    def test_change_complains_if_not_given_enough_money(self):
        with self.assertRaises(AssertionError) as e:
            coins = self.num_fun.change(2, 1)
        expected = "Hey! That isn't enough!"
        self.assertEqual(e.exception.msg, expected)
