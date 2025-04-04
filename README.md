## Turing Machine Simulator

This project is a Turing Machine simulator designed for testing and validating state machine implementations. 
It provides a flexible environment for defining, running, and debugging Turing Machine models with automatic testing, performance tracking, and error reporting.
I needed it while checking my solutions while learning computational theory in one of my courses!

## Examples

Take a look at `examples/ex1` to see how I used this to test my design for a TM that identifies the language $L = \{a^nb^mc^{(m+n)}:m,n>0\}$!

### Key Features

- **State-Based Computation**: Define your own Turing Machine by specifying the states and transitions. This allows for testing different types of Turing Machine logic, from simple string recognition to more complex automata.
- **Tape Simulation**: The machine operates on a tape, which can grow infinitely in either direction. This enables testing of non-trivial string manipulation and machine behavior under different input conditions.
- **Performance Monitoring**: The simulator includes built-in analytics that tracks the success rate of test cases and the number of iterations each Turing Machine runs, helping to monitor performance and identify inefficiencies.
- **Error Handling**: Custom errors are raised for invalid transitions, infinite loops, or other unexpected behaviors, making it easy to debug and refine the Turing Machine logic.

### Cool Technical Aspects

- **Dynamic Tape Management**: The simulator uses a defaultdict to simulate an infinite tape, dynamically expanding in both directions as needed, which is a true representation of the Turing Machine's theoretical capability.
- **Custom Transition Logic**: You can fully define the state transitions, including the symbol to write, the head movement (left or right), and the next state, providing deep control over the machine's behavior.
- **Automated Testing**: The built-in testing framework automatically runs a series of tests with randomly generated input strings, making it easy to validate that the Turing Machine behaves correctly across a range of cases.
- **Iterative Debugging**: With the debug flag, you can step through the machine’s operations and view real-time outputs of tape updates and state transitions. This is especially useful for understanding how the Turing Machine processes complex strings.

### Use Cases

- **Turing Machine Theory**: Ideal for students and researchers studying theoretical computer science concepts like decidability, computability, and automata theory.
- **State Machine Prototyping**: Use this simulator to quickly prototype and test new state machine logic or automata-based algorithms.
- **Educational Tool**: A great tool for students who want to play around with Turing Machines!
