import sys
import math


class FactorFinder:
    def __init__(self):
        self.prime_numbers = set()

    def run(self):
        print('''
Factor Finder

A number's factors are two numbers that, when multiplied with each
other, produce the number. For example, 2 x 13 = 26, so 2 and 13 are
factors of 26. 1 x 26 = 26, so 1 and 26 are also factors of 26. We
say that 26 has four factors: 1, 2, 13, and 26.

If a number only has two factors (1 and itself), we call that a prime
number. Otherwise, we call it a composite number.

Can you discover some prime numbers?
''')

        while True:
            print('Enter a positive whole number to factor (or QUIT):')
            response = input('> ').upper()
            if response == 'QUIT':
                sys.exit()

            if response.isdecimal() and int(response) > 0:
                number = int(response)
                factors = self.find_factors(number)
                self.display_factors(number, factors)

    def find_factors(self, number):
        factors = set()

        for i in range(1, int(math.sqrt(number)) + 1):
            if number % i == 0:
                factors.add(i)
                factors.add(number // i)

        return sorted(list(factors))

    def display_factors(self, number, factors):
        prime_status = "prime" if len(factors) == 2 else "composite"
        print(f"Multipliers of {number}: {factors}")
        print(f"Number {number} is {prime_status}.\n")


if __name__ == '__main__':
    factor_finder = FactorFinder()
    factor_finder.run()
