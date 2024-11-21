import argparse
from typing import Callable, Tuple
from abc import ABC, abstractmethod
from unittest.mock import DEFAULT

from turing import REJECT, ACCEPT
from .tape import Tape

DEFAULT_STR_MIN_LENGTH = 3
DEFAULT_STR_MAX_LENGTH = 500
DEFAULT_MAX_TESTS = 50
DEFAULT_MAX_ITERATIONS = 5000000

class TuringError(Exception):
    """Base class for Turing Machine Errors."""
    pass

class StateTransitionError(TuringError):
    """
    Occurs when the transition between states isn't formatted correctly.
    Make sure you are returning -> (char_to_write: str, direction: str, new_state: func)
    """
    pass

class TooManyIterationsError(TuringError):
    """
    Occurs when the machine takes too long to compute a single string.
    Probably got stuck in a loop!
    """
    pass

class TuringMachine(ABC):
    def __init__(self, starting_state: Callable[[str], Tuple[str, str, Callable]],
                 min_gen_str_len: int = DEFAULT_STR_MIN_LENGTH,
                 max_gen_str_len: int = DEFAULT_STR_MAX_LENGTH,
                 max_tests: int = DEFAULT_MAX_TESTS,
                 max_iterations: int = DEFAULT_MAX_ITERATIONS
                 ):
        self.starting_state = starting_state
        self.min_length = min_gen_str_len
        self.max_length = max_gen_str_len
        self.num_tests = max_tests
        self.max_iterations = max_iterations

    @abstractmethod
    def gen_random_tape(self, *args, **kwargs) -> Tape:
        pass

    @abstractmethod
    def gen_passing_tape(self, *args, **kwargs) -> Tape:
        pass

    @abstractmethod
    def gen_tape(self, *args, **kwargs) -> Tape:
        pass

    @abstractmethod
    def check(self, string) -> str:
        pass

    def resolve(self, tape, debug=False):
        """
        Resolves a single tape and returns the result (accept or reject)
        """
        # save input str
        input_str = tape.message(do_format=False)

        # setup tm
        state = self.starting_state
        iterations = 0

        # start loop
        while iterations < self.max_iterations:
            if debug: # print the tape before
                print(f'{state.__name__}(\'{tape.read()}\')')
                print(tape)
            
            z = state(tape.read())
            try:
                c, direction, new_state = z
            except Exception:
                raise StateTransitionError(f'in state {state.__name__}, input={tape.read()}\n{tape.__str__()}')
            
            #update state
            state = new_state
            if state == REJECT or state == ACCEPT:
                result = state

                if debug:
                    expected = self.check(input_str)
                    if expected == result:
                        print('✅', 'expected:', expected, 'result:', result)
                    else:
                        print('❌', 'expected:', expected, 'result:', result)
                        print('input:', input_str)

                return result

            # update tape
            tape.write(c)
            tape.move(direction)

            # update count
            iterations = iterations + 1
        message = f'Too many iterations on tape: {input_str}.\nUse turingmachine.resolve({input_str}, debug=True) to see where the problem is.'
        raise TooManyIterationsError(message)

    def main(self):
        # Set up argument parser
        parser = argparse.ArgumentParser(description='Initialize a Turing machine tape with a string.')
        parser.add_argument('input_string', nargs='?', type=str, help='The string to initialize the tape with.')
        
        # Parse the arguments
        args = parser.parse_args()

        # if given an argument use that string
        if args.input_string:
            result = self.resolve(self.gen_tape(args.input_string), debug=True)
            expected = self.check(args.input_string)
            print('expected:', expected, 'result', result)

        # otherwise do many tests
        else:
            # analytics
            test_count, correct, incorrect = 0, 0, 0

            # loop over the tests
            while test_count < self.num_tests:
                # create the tape
                tape = self.gen_tape()
                generated_str = tape.__str__()

                # do the calculation
                result = self.resolve(tape)

                # get correct answer
                expected = self.check(generated_str)

                # print result
                if expected == result:
                    print('✅', 'expected:', expected, 'result:', result)
                    correct = correct + 1
                else:
                    print('❌', 'expected:', expected, 'result:', result)
                    print('input:', generated_str)
                    incorrect = incorrect + 1

                # iterate
                test_count = test_count + 1
            
            # print analytics
            print('\n', correct, '/', incorrect + correct, (correct / (correct + incorrect)) * 100, '%')