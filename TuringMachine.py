from collections import defaultdict

class TuringMachine:
    def __init__(self, s, default_symbol=' '):
        """
        Initializes the Turing machine tape.
        
        Parameters:
            default_symbol (str): The default symbol for uninitialized tape cells.
        """
        self.tape = defaultdict(lambda: default_symbol)  # Simulate infinite cells
        self.head_position = 0  # Start the tape head at position 0
        self.initialize_tape(s)
    
    def initialize_tape(self, s):
        """
        Initializes the tape with the given string and sets the head to the first character.
        
        Parameters:
            s (str): The initial string to populate the tape.
        """
        for i, char in enumerate(s):
            self.tape[i] = char
        self.head_position = 0  # Start the head at the first character

    def read(self):
        """Reads the symbol under the tape head."""
        return self.tape[self.head_position]

    def write(self, symbol):
        """Writes a symbol to the cell under the tape head."""
        self.tape[self.head_position] = symbol

    def move(self, direction):
        """
        Moves the tape head in the specified direction.
        
        Parameters:
            direction (str): 'L' to move left, 'R' to move right.
        """
        if direction == 'L':
            self.head_position -= 1
        elif direction == 'R':
            self.head_position += 1
        else:
            raise ValueError("Direction must be 'L' (left) or 'R' (right).")

    def __str__(self):
        """
        Returns a string representation of the tape for debugging.
        Shows a limited segment around the head.
        """
        min_pos = min(self.tape.keys())
        max_pos = max(self.tape.keys())
        tape_str = ''.join(self.tape[i] for i in range(min_pos, max_pos + 1))
        head_indicator = ' ' * (self.head_position - min_pos) + '^'
        return f"Tape: {tape_str}\n      {head_indicator}"


# # Example Usage
# tape = TuringMachineTape()
# print(tape)  # Initially empty tape

# tape.write('1')
# tape.move('R')
# tape.write('0')
# tape.move('R')
# tape.write('1')
# tape.move('L')
# print(tape)  # Shows a segment of the tape
