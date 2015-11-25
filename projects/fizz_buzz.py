def fizz_buzz_to_one_hundred():
    '''
    Prints the numbers from 1 to 100, but prints "Fizz" instead of the
    number for multiples of three, "Buzz" for multiples of five, and "FizzBuzz"
    for multiples of both three and five.
    '''
    for i in range(1, 101):
        if i % 3 == 0 and i % 5 == 0:
            printable = "FizzBuzz"
        elif i % 3 == 0:
            printable = "Fizz"
        elif i % 5 == 0:
            printable = "Buzz"
        else:
            printable = i
        print(printable)
