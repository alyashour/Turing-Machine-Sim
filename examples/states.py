
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
    if c in ['x', 'b', 'c']:
        return c, LEFT, q2

    if c in [' ']:
        return c, RIGHT, q9
    
    if c in ['a']:
        return c, LEFT, q8
    
def q3(c):
    if c in ['c', ' ']:
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
        return 'x', LEFT, q10

def q5(c):
    if c in ['b']:
        return c, LEFT, q5
    
    if c in ['x']:
        return c, RIGHT, q6
    
    else:
        return c, RIGHT, qreject

def q6(c):
    if c in ['b']:
        return 'x', RIGHT, q4

    if c in ['a', 'c', ' ']:
        return c, RIGHT, qreject

def q8(c):
    if c in ['a']:
        return c, LEFT, q8

    if c in ['x']:
        return c, RIGHT, q3
    
    if c in ['b', 'c']:
        return c, RIGHT, qreject

def q9(c):
    if c in ['x']:
        return c, RIGHT, q9
    
    if c in ['b']:
        return 'x', RIGHT, q4

def q10(c):
    if c in ['b']:
        return c, LEFT, q5
    
    if c in ['x']:
        return c, LEFT, q10

    if c in [' ']:
        return c, RIGHT, qaccept
    
    if c in ['a', 'c']:
        return c, RIGHT, qreject

def qreject(c):
    return c, RIGHT, "Reject"

def qaccept(c):
    return c, RIGHT, "Accept"
