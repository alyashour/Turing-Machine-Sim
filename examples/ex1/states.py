from turing import REJECT, ACCEPT, LEFT, RIGHT

def qreject(c):
    return c, RIGHT, REJECT

def qaccept(c):
    return c, RIGHT, ACCEPT

def q0(c):
    if c == 'a':
        return 'x', RIGHT, q1
    if c in ['b', 'c']:
        return c, RIGHT, qreject

def q1(c):
    if c == ' ':
        return c, LEFT, q2

    return c, RIGHT, q1

def q2(c):
    if c == 'x':
        return c, LEFT, q2
    if c in ['a', 'b']:
        return c, RIGHT, qreject
    if c == 'c':
        return 'x', LEFT, q3

def q3(c):
    if c == ' ':
        return c, RIGHT, q3
    return c, LEFT, q4

def q4(c):
    if c == 'a':
        return 'x', RIGHT, q1
    if c == 'b':
        return 'x', RIGHT, q5
    if c == 'c':
        return c, RIGHT, qreject
    if c == 'x':
        return c, RIGHT, q4

def q5(c):
    if c == ' ':
        return c, LEFT, q6
    return c, RIGHT, q5

def q6(c):
    if c in ['a', 'b']:
        return c, LEFT, qreject
    if c == 'x':
        return c, LEFT, q6
    if c == 'c':
        return 'x', LEFT, q7

def q7(c):
    if c == ' ':
        return c, RIGHT, q8
    return c, LEFT, q7

def q8(c):
    if c in ['a', 'c']:
        return c, RIGHT, qreject
    if c == 'b':
        return 'x', RIGHT, q5
    if c == ' ':
        return c, RIGHT, qaccept
    if c == 'x':
        return c, RIGHT, q8