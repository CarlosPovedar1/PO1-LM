


#-->(null): a instruction that does not do anything




#control structure
def Conditional( lista:list): 
    """Executes B1 if condition is true and
    B2 if condition is false. B1 and B2 can be a single command or a Block"""
    list[0] = si
    list[1]= condition
    list[2]= B1
    list[3]= B2
    x = True
    if len(lista) >4:
        return False
    
    if si == "<if>":
        x= True
    else:
        x= False
    #falta saber si las condiciones son verdaderas

    return x

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

#command defvar

def defvar (lista:list):
    """where name is a variable’s name and n is a number or a
    constant used initializing the variable."""
    lista[0] = defvar
    lista[1] =  name
    lista[2] = n
    x = True
    if len(lista) >4:
        x = False

    if defvar !="<defvar>":
        x= False
    if str != name:
        x= False
    if int != type(n):
        x= False
    return x

#command =
def equals(name, n):
    """where name is a variable’s name and n is a number or a constant
    The result of this instruction is to assign the value of the number n to the
    variable."""
    lista[0] = equal
    lista[1] =  name
    lista[2] = n
    x = True
    if len(lista) >4:
        x= False

    if equal !="<=>":
        x= False
    if str != name:
        x= False
    if int != type(n):
        x= False
    return x
#command move
def move(n):
    """where n is a number or a variable or a constant. The robot
    should move n steps forward."""
    lista[0] = move
    lista[1] = n
    x = True
    if len(lista) >2:
        x= False

    if move !="<move>":
        x= False
    if int != type(n):
        x= False
    return x
#command skip
def skip(lista:list):
    """where n is a number or a variable or a constant. The robot
    should jump n steps forward."""
    lista[0] = skip
    lista[1] = n
    x = True
    if len(lista) >2:
        x= False

    if skip !="<skip>":
        x= False
    if int != type(n):
        x= False
    return x
#command turn 
def turn(lista:list):
    """where D can be :left, :right, or :around (defined as constants).
    The robot should turn 90 degrees in the direction of the parameter in the
    first to cases, and 180 in the last case."""
    lista[0] = turn
    lista[1] = D
    x = True
    if len(lista) >2:
        x= False

    if turn !="<turn>":
        x= False
    if D !="<left>" or D !="<right>" or D!= "<around>":
        x= False
    return x
#command face 
def face(lista:list):
    """where O can be :north, :south, :east, or :west (all constants).
    The robot should turn so that it ends up facing direction O."""
    lista[0] = face
    lista[1] = O
    x = True
    if len(lista) >2:
        x= False

    if face !="<face>":
        x= False
    if  O!="<north>" or O !="<south>" or O!= "<east>" or O!="<west>":
        x= False
    
    return x
# command put
def put(lista:list):
    """where X corresponds to either :balloons or :chips, and n is a
    number or a variable. The Robot should put n X’s."""
    lista[0] = put
    lista[1] = X
    lista[2] = n
    if len(lista) >3:
        x= False

    if put !="<put>":
        x= False
    if  X!="<balloons>" or X!="<chips>" :
        x= False
    return x
#command pick
def pick(lista:list):
    """where X is either :balloons or :chips, and n is a number or
    a variable. The robot should pick n X’s."""
    lista[0] = pick
    lista[1] = X
    lista[2] = n
    x = True
    if len(lista) >3:
        x= False

    if pick !="<pick>":
        x= False
    if  X!="<balloons>" or X!="<chips>" :
        x= False
    if int != type(n):
        x= False
    return x
#command move-dir()
def move_dir(lista:list):
    """where n is a number or a variable. D is one of :front,
    :right, :left, :back. The robot should move n positions to the front,
    to the left, the right or back and end up facing the same direction as it
    started."""
    lista[0] = move
    lista[1] = n
    lista[2] = D
    x = True
    if len(lista) >3:
        x= False

    if pick !="<pick>":
        x= False
    if  D!="<front>" or D!="<right>" or D!="<left>" or D!="<back>":
        x= False
    if int != type(n):
        x= False
    return x
#command run_dirs
def run_dirs(lista:list):
    """where Ds is a non-empty list of directions: :front, :right,
    :left, :back. The robot should move in the directions indicated by the
    list and end up facing the same direction as it started."""
    lista[0] = run
    lista[1] = Ds
    
    x = True
    if len(lista) >2:
        x= False

    if run !="<run>":
        x= False
    if  Ds!="<front>" or Ds!="<right>" or Ds!="<left>" or Ds!="<back>":
        x= False
   
    return x
#command move-face
def move_face(n,O):
    """here n is a number or a variable. O is :north, :south,
    :west, or :east. The robot should face O and then move n steps."""
    pass