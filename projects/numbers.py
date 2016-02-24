class Numbers(object):
    def listonacci_to(self, n):
        """Returns a series of Fibonacci numbers from 1 to n."""
        numbers = []
        i, j = 1, 1
        for number in range(1, n+1):
            numbers.append(i)
            i, j = j, i+j
        return numbers

    def fibosniper(self, n):
        """Returns the nth Fibonacci number."""
        return self.listonacci_to(n)[-1]

    def change(self, cost, pay):
        """Returns a dict with the change owed in number of dollars and coins
        based on a cost and payment amount.
        """
        assert (pay > cost), "Hey! That isn't enough!"
        purse = {1.00: 0, 0.25: 0, 0.10: 0, 0.05: 0, 0.01: 0}
        coins = [1.00, 0.25, 0.10, 0.05, 0.01]
        change = pay - cost
        for coin in coins:
            while change >= coin:
                purse[coin] += 1
                change -= coin
        return purse

    def gimme_prime(self):
        """Generates an infinite sequence of prime numbers."""
        sieve = {}
        i = 2

        while True:
            if i not in sieve:
                yield i
                # Capture the squares of primes for subsequent sieving and add
                # the prime as its value as a starting point for getting
                # multiples.
                sieve[i**2] = [i]
            else:
                for j in sieve[i]:
                    # Add the next multiple of a previous prime with its prime
                    # factor(s) to the sieve.
                    sieve.setdefault(j + i, []).append(j)
                del sieve[i]  # Remove sieved multiple as it has been sieved.
            i += 1

    def primo_sniper(self, n):
        """Returns the nth prime number."""
        prime_num_gen = self.gimme_prime()
        return [next(prime_num_gen) for i in range(n)][-1]

    def binary_to_int(self, binary):
        """Accepts a binary and returns an integer."""
        assert type(binary) == str, 'Binary must be str.'
        integer = 0
        for digit_place, digit in enumerate(binary[::-1]):
            if digit == '1':
                integer += 2**digit_place
        return integer

    def int_to_binary(self, i):
        """Accepts a number and converts it to binary as a str."""
        assert type(i) == int, 'Number must be int.'
        binary_digits = []
        while i:
            i, remainder = self.divide_with_remainder(i, 2)
            binary_digits.insert(0, str(remainder))
        return ''.join(binary_digits)

    def divide_with_remainder(self, numerator, denominator):
        """Returns the dividend of two integers with a remainder."""
        dividend, remainder = numerator // denominator, numerator % denominator
        return (dividend, remainder)


def loop_factorial(i):
    multiplier = i - 1
    while multiplier:
        i *= multiplier
        multiplier -= 1
    return i


def factorial(i):
    if i == 0:
        return 1
    return i * factorial(i-1)


def factor(i):
    fs = [j for j in range(1, i+1) if i % j == 0]
    return fs if fs else None


def find_prime_factors(i):
    pfs = [j for j in factor(i) if is_prime(j)]
    return pfs if pfs else None


def is_prime(i):
    """Returns a boolean if the number is prime or not."""
    return True if len(factor(i)) == 2 else False
