import unittest

from lib import numbers


class TestNumbers(unittest.TestCase):
    def setUp(self):
        self.num_fun = numbers.Numbers()

    def test_returns_list_of_n_length(self):
        nums = self.num_fun.listonacci_to(42)
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
            self.num_fun.change(2, 1)
        expected = "Hey! That isn't enough!"
        self.assertEqual(e.exception.msg, expected)

    def test_gimme_prime_yields_prime_numbers_from_generator(self):
        prime_num_gen = self.num_fun.gimme_prime()
        primes = [next(prime_num_gen) for i in range(3)]
        expected = [2, 3, 5]
        self.assertEqual(primes, expected)

    def test_primo_sniper_returns_nth_prime_number(self):
        prime_number = self.num_fun.primo_sniper(42)
        self.assertEqual(prime_number, 181)

    def test_int_to_binary_returns_binary_number_as_str(self):
        binary = self.num_fun.int_to_binary(8)
        self.assertEqual(binary, '1000')

    def test_binary_to_int_returns_int_for_binary(self):
        integer = self.num_fun.binary_to_int('1010')
        self.assertEqual(integer, 10)

    def test_loop_factorial(self):
        self.assertEqual(numbers.loop_factorial(4), 24)

    def test_factorial(self):
        self.assertEqual(numbers.factorial(5), 120)
