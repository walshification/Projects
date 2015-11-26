def listonacci_to(n):
    '''Returns a series of Fibonacci numbers from 1 to n.'''
    numbers = []
    i, j = 1, 1
    for number in range(1, n+1):
        numbers.append(i)
        i, j = j, i+j
    return numbers


def fibosniper(n):
    return listonacci_to(42)[-1]


if __name__ == '__main__':  # pragma no cover
    from sys import argv
    for number in listonacci_to(int(argv[1])):
        print(number)
