def fizz_buzz_to_one_hundred():
    '''
    Prints the numbers from 1 to 100, but prints "Fizz" instead of the
    number for multiples of three, "Buzz" for multiples of five, and "FizzBuzz"
    for multiples of both three and five.
    '''
    numbers = []
    for i in range(1, 101):
        numbers.append('Fizz' * (i % 3 == 0) + 'Buzz' * (i % 5 == 0) or i)
    return numbers


if __name__ == '__main__':  # pragma no cover
    for i in fizz_buzz_to_one_hundred():
        print(i)
