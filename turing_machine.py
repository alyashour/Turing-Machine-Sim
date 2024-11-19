import random
import argparse
from TuringMachine import TuringMachine

RIGHT = 'R'
LEFT = 'L'

def q0(c):
    if c in ['b', 'c', ' ']:
        return c, RIGHT, qreject

    if c in ['a']:
        return 'x', RIGHT, q1
    
    raise ValueError

def q1(c):
    if c in [' ']:
        return c, RIGHT, qreject
    
    if c in ['c']:
        return 'x', LEFT, q2
    
    if c in ['a', 'b', 'x']:
        return c, RIGHT, q1

def q2(c):
    if c in ['a', 'b', 'c']:
        return c, LEFT, q2
    
    if c in ['x']:
        return c, RIGHT, q3
    
def q3(c):
    if c in ['x', 'c', ' ']:
        return c, RIGHT, qreject
    
    if c in ['a']:
        return 'x', RIGHT, q1

    if c in ['b']:
        return 'x', RIGHT, q4

def q4(c):
    if c in ['b', 'x']:
        return c, RIGHT, q4
    
    if c in ['a', ' ']:
        return c, RIGHT, qreject
    
    if c in ['c']:
        return 'x', LEFT, q5

def q5(c):
    if c in ['a', 'b', 'c']:
        return c, LEFT, q5
    
    if c in ['x']:
        return c, RIGHT, q6

def q6(c):
    if c in ['x']:
        return c, RIGHT, q7
    
    if c in ['b']:
        return 'x', RIGHT, q4

    if c in ['a', 'c', ' ']:
        return c, RIGHT, qreject

def q7(c):
    if c in ['x']:
        return c, RIGHT, q7
    
    if c in ['a', 'b', 'c']:
        return c, RIGHT, qreject

    if c in [' ']:
        return c, RIGHT, qaccept

def qreject(c):
    return c, RIGHT, "Reject"

def qaccept(c):
    return c, RIGHT, "Accept"

def gen_random_tape(min_length, max_length):
    if min_length > max_length or min_length < 0:
        raise ValueError("Invalid length bounds. Ensure 0 <= min_length <= max_length.")
    
    length = random.randint(min_length, max_length)
    return ''.join(random.choices('abc', k=length))

def gen_passing_tape(n: int, m: int):
    if n <= 0 or m <= 0:
        raise ValueError("n and m must be non-negative integers.")
    
    # Create the string
    result = 'a' * n + 'b' * m + 'c' * (m + n)
    return result

def gen_tape(min_length, max_length):
    if random.random() < 0.5:
        return gen_random_tape(min_length, max_length)
    else:
        while True:
            length = int(random.random() * max_length) # random total legnth
            mpn = int(random.random() * length) / 2 # random m + n length
            n = int(random.random() * mpn) # random make up of m and n
            m = int(mpn - n)
            assert mpn + m + n <= length
            if mpn + m + n >= min_length and mpn + m + n <= max_length and m > 0 and n > 0 and mpn > 0:
                break
        
        return gen_passing_tape(n, m)

def main():
    # Set up argument parser
    parser = argparse.ArgumentParser(description='Initialize a Turing machine tape with a string.')
    parser.add_argument('input_string', nargs='?', type=str, help='The string to initialize the tape with.')
    
    # Parse the arguments
    args = parser.parse_args()

    state = q0
    tape = TuringMachine(gen_tape(3, 200))
    print(tape)
    # TEMP
    count = 0
    while (count < 500):
        r = tape.read()
        z = state(r)
        print('state:', state.__name__, 'cell:', r, 'z:', z)
        c, direction, new_state = z
        
        
        #update state
        state = new_state
        if state == "Reject" or state == "Accept":
            break

        # update tape
        tape.write(c)
        tape.move(direction)
        
        # update count
        count = count + 1
        print(tape)

    print(tape, state)

main()