
#-->(null): a instruction that does not do anything




#control structure
def Conditional( condition, B1, B2): 
    """Executes B1 if condition is true and
    B2 if condition is false. B1 and B2 can be a single command or a Block"""
    pass

def Repeat( condition, B):
    """Executes B while condition is true. B can
    be a single command or a block."""
    pass

def RepeatTimes(n, B):
    """ where n is a variable or a number. B is
    executed n times. B is a cingle command or a block."""
    pass
def FunctionDefinition(defun, name, Params,Cs):
    """where name is the function
    name, (Params) is a list of parameter names for the function (separated
    by spaces) and Cs is a sequence of commands for the function."""
    pass
    #A function call is the function’s name followed by parameter values within
    #parenthesis, as in (funName a1 a2 a3).
    pass
def cond():
    "condicion"
    pass

#----------------------------commands----------------------------------

#command defvar

def defvar (name, n):
    """where name is a variable’s name and n is a number or a
    constant used initializing the variable."""
    name = n
    return name

#command =
def equals(name, n):
    """where name is a variable’s name and n is a number or a constant
    The result of this instruction is to assign the value of the number n to the
    variable."""
    name =n
    return name
#command move
def move(n):
    """where n is a number or a variable or a constant. The robot
    should move n steps forward."""
    pass
#command skip
def skip(n):
    """where n is a number or a variable or a constant. The robot
    should jump n steps forward."""
    pass
#command turn 
def turn(D):
    """where D can be :left, :right, or :around (defined as constants).
    The robot should turn 90 degrees in the direction of the parameter in the
    first to cases, and 180 in the last case."""
    pass
#command face 
def face(O):
    """where O can be :north, :south, :east, or :west (all constants).
    The robot should turn so that it ends up facing direction O."""
    pass
# command put
def put(x, n):
    """where X corresponds to either :balloons or :chips, and n is a
    number or a variable. The Robot should put n X’s."""
    pass
#command pick
def pick(x,n):
    """where X is either :balloons or :chips, and n is a number or
    a variable. The robot should pick n X’s."""
    pass
#command move-dir()
def move_dir(n, D):
    """where n is a number or a variable. D is one of :front,
    :right, :left, :back. The robot should move n positions to the front,
    to the left, the right or back and end up facing the same direction as it
    started."""
    pass
#command run_dirs
def run_dirs(Ds):
    """where Ds is a non-empty list of directions: :front, :right,
    :left, :back. The robot should move in the directions indicated by the
    list and end up facing the same direction as it started."""
    pass
#command move-face
def move_face(n,O):
    """here n is a number or a variable. O is :north, :south,
    :west, or :east. The robot should face O and then move n steps."""
    pass