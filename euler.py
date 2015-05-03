# -*- coding: utf-8 -*-
'''Implementation of various project euler challenges

Solved challenges by id:
1: Multiplies of 3 and 5
2: Even Fibonacci numbers
3: Largest prime factor
4: in progress - Largest palindrome product
'''
import math


def is_palindrome(number):
    ''' Returns true if number is a palindrome

    >>> is_palindrome(123)
    False
    >>> is_palindrome(9009)
    True
    >>> is_palindrome(99)
    True
    >>> is_palindrome(909)
    False
    >>> is_palindrome(1)
    False
    '''
    number = str(number)
    length = len(number)
    # only even length numbers work
    if length % 2 != 0:
        return False
    half = int(length/2)
    # split the number in half and reverse the second half with [::-1]
    first, second = number[:half], number[half:][::-1]
    if first != second:
        return False
    return True


def largest_palindrome_product(n):
    '''Returns largest palindrome made from the product of two n-digit numbers.

    >>> largest_palindrome_product(2)
    9009
    '''
    # created the largest n digit number
    x = int('9' * n)
    # greatest possible product with n digit
    y = x * x
    for i in range(y, -1, -1):
        if not is_palindrome(i):
            continue
        y = math.sqrt(i)
        if y.is_integer():
            break
    return y


def next_prime(prime):
    '''Returns the succedding prime

    >>> next_prime(13)
    17
    >>> next_prime(9967)
    9973
    '''
    prime += 1
    while True:
        if (not (prime % 2 == 0 and prime > 2) and (
                all(prime % i for i in range(3,
                                             int(math.sqrt(prime)) + 1,
                                             2)))):
            break
        prime += 1
    return prime


def largest_prime_factor(number):
    ''' Determine largest prime factor of the number.

    >>> largest_prime_factor(13195)
    29
    '''
    # float.is_integer
    largest = 2
    while True:
        value = number/largest
        if not value.is_integer():
            prime = next_prime(largest)
            if prime > number:
                break
            largest = prime
        else:
            number = value
    return largest


def sum_of_even_fibonacci(limit):
    '''Returns sum of the even-valued terms in the
    Fibonacci sequence whose values do not exceed the limit.

    >>> sum_of_even_fibonacci(100)
    44
    '''
    sequence = [1, 2]
    while True:
        term = sequence[-2] + sequence[-1]
        if term > limit:
            break
        sequence.append(term)
    return sum([i for i in sequence if i % 2 == 0])


def multiplies_of(numbers, limit):
    '''Find the sum of all the multiples of numbers below limit.

    >>> multiplies_of([3, 5], 10)
    23
    '''
    result = 0
    for i in range(limit):
        for j in numbers:
            if i % j == 0:
                result += i
    return result


if __name__ == '__main__':
    import doctest
    doctest.testmod()
