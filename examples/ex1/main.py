import random

from turing.turing_machine import TuringMachine
from turing.tape import Tape
from states import *

class TM1(TuringMachine):
    def __init__(self):
        super().__init__(q0, min_gen_str_len=5, max_gen_str_len=500, max_tests=5000)

    def gen_random_tape(self):
        if self.min_length > self.max_length or self.min_length < 0:
            raise ValueError("Invalid length bounds. Ensure 0 <= min_length <= max_length.")
        
        length = random.randint(self.min_length, self.max_length)
        return Tape(''.join(random.choices('abc', k=length)))

    def gen_passing_tape(self, n: int, m: int):
        if n <= 0 or m <= 0:
            raise ValueError("n and m must be non-negative integers.")
        
        # Create the string
        result = 'a' * n + 'b' * m + 'c' * (m + n)
        return Tape(result)

    def gen_tape(self, s: str = None) -> Tape:
        # if a string is given, return that tape
        if s:
            return Tape(s)
        
        # otherwise, randomly pick between a passing and non-passing tape
        if random.random() < 0.5:
            return self.gen_random_tape()
        else:
            while True:
                length = int(random.random() * self.max_length) # random total legnth
                mpn = int(random.random() * length / 2)  # random m + n length
                n = int(random.random() * mpn) # random make up of m and n
                m = int(mpn - n)
                assert mpn + m + n <= length
                assert n + m == mpn

                if self.min_length <= mpn + m + n <= self.max_length and m > 0 and n > 0 and mpn > 0:
                    break
            
            return self.gen_passing_tape(n, m)

    def check(self, string) -> str:
        a, b, c = 0, 0, 0
        last_char = 'a'
        if string[0] != 'a':
            return REJECT
        for char in string:
            if char == 'a' and last_char == 'a':
                a = a + 1
            elif char == 'b' and last_char in ['a', 'b']:
                b = b + 1
                last_char = 'b'
            elif char == 'c' and last_char in ['b', 'c']:
                c = c + 1
                last_char = 'c'
        return ACCEPT if a + b == c else REJECT

if __name__ == "__main__":
    tm = TM1()

    # run a single test
    tape = Tape('aababcbabcbcaccbaccacabcbbacabbcaccacbaaccbabcabbb') # create the tape
    tm.resolve(tape, debug=True)

    # run many iterations
    tm.main()