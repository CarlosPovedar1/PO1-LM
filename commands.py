


#-->(null): a instruction that does not do anything




#control structure
def Conditional(token): 
    """Executes B1 if condition is true and
    B2 if condition is false. B1 and B2 can be a single command or a Block"""
    if token.type =="if":
        return True
    else:
        return False

def Repeat( lista: list):
    """Executes B while condition is true. B can
    be a single command or a block."""
    lista[0] =loop
    x = True
    
    if len(lista) >4:
        return False
    if loop != "<loop>":
        return False
    #falta saber la condicion de loop 


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



def isdefvar (token):
    """where name is a variable’s name and n is a number or a
    constant used initializing the variable."""
    
    if token.type =="defvar":
        return True
    else:
        return False
def defvar(lista,i):
    respuesta = False
    if lista[i+1].type== 'nombre':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta

#command =
def isequals(token):
    """where name is a variable’s name and n is a number or a constant
    The result of this instruction is to assign the value of the number n to the
    variable."""
    if token.type =="equals":
        return True
    else:
        return False
def equals(lista,i):
    
    respuesta = False
    if lista[i+1].type== 'nombre':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta
#command move
def move(token):
    """where n is a number or a variable or a constant. The robot
    should move n steps forward."""
    if token.type =="move":
        return True
    else:
        return False
    
def move(lista,i):
    respuesta = False
    if lista[i+1].type == 'number':
        respuesta =True
        i+=1
    return respuesta
    
#command skip
def skip(token):
    """where n is a number or a variable or a constant. The robot
    should jump n steps forward."""
    if token.type =="defvar":
        return True
    else:
        return False
#command turn 
def turn(token):
    """where D can be :left, :right, or :around (defined as constants).
    The robot should turn 90 degrees in the direction of the parameter in the
    first to cases, and 180 in the last case."""
    if token.type =="turn":
        return True
    else:
        return False
    return x
#command face 
def face(token):
    """where O can be :north, :south, :east, or :west (all constants).
    The robot should turn so that it ends up facing direction O."""
    if token.type =="face":
        return True
    else:
        return False
# command put
def isput(token):
    """where X corresponds to either :balloons or :chips, and n is a
    number or a variable. The Robot should put n X’s."""
    if token.type =="put":
        return True
    else:
        return False
def put(lista,i):
    respuesta = False
    if lista[i+1].type== 'nombre':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta

#command pick
def ispick(token):
    """where X is either :balloons or :chips, and n is a number or
    a variable. The robot should pick n X’s."""
    if token.type =="pick":
        return True
    else:
        return False
    
def pick(lista,i):
    """where X is either :balloons or :chips, and n is a number or
    a variable. The robot should pick n X’s."""
    respuesta = False
    if lista[i+1].type== 'nombre':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta
#command move-dir()
def ismove_dir(token):
    """where n is a number or a variable. D is one of :front,
    :right, :left, :back. The robot should move n positions to the front,
    to the left, the right or back and end up facing the same direction as it
    started."""
    if token.type =="move_dir":
        return True
    else:
        return False
    
def move_dir(lista,i):
    respuesta = False
    if lista[i+1].type== 'nombre':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta
#command run_dirs
def run_dirs(token):
    """where Ds is a non-empty list of directions: :front, :right,
    :left, :back. The robot should move in the directions indicated by the
    list and end up facing the same direction as it started."""
    if token.type =="defvar":
        return True
    else:
        return False
#command move-face
def ismove_face(token):
    """here n is a number or a variable. O is :north, :south,
    :west, or :east. The robot should face O and then move n steps."""
    if token.type =="move_face":
        return True
    else:
        return False
def move_face(lista,i):
    respuesta = False
    if lista[i+1].type== 'nombre':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta
    
def iscommand(token):
    if token.type =="defvar":
        return True
    elif token.type =="equals":
        return True
    elif token.type =="move":
        return True
    elif token.type =="skip":
        return True
    elif token.type =="turn":
        return True
    elif token.type =="face":
        return True
    elif token.type =="put":
        return True
    elif token.type =="pick":
        return True
    elif token.type =="move_dir":
        return True
    elif token.type =="run_dirs":
        return True
    elif token.type =="move_face":
        return True
    else:
        return False