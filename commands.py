


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
#------------------------condicionals----------------------------------------
def cond(lista,i):
    "condicion"
    respuesta = False
    contador= 0
    if lista[i].type == 'facing_conditional':
        respuesta,i =facing_conditional(lista,i)
    elif lista[i].type == 'blocked_conditional':
        respuesta = True
        i+=1
    elif lista[i].type == 'put_conditional':
        respuesta,i =put_conditional(lista,i)
    elif lista[i].type == 'pick_conditional':
        respuesta,i =pick_conditional(lista,i)
    elif lista[i].type == 'move_conditional':
        respuesta,i =move_conditional(lista,i)
    elif lista[i].type == 'zero_conditional':
        respuesta,i =zero_conditional(lista,i)
    elif lista[i].type == 'not_conditional':
        if lista[i+1].type == 'left_parenth':
            contador-=1
            i+=1
        respuesta,i =not_conditional(lista,i)
        if lista[i+1].type =='right_parenth':
            contador +=1
            i+=1
        if contador != 0:
            respuesta= False
        
        
    return respuesta,i

    
def facing_conditional(lista,i):
    respuesta = False
    if lista[i+1].type == 'cardinal':
        respuesta =True
        i+=1
    return respuesta,i
def put_conditional(lista,i):
    respuesta = False
    if lista[i+1].type== 'i_objects':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta,i

def pick_conditional(lista,i):
    respuesta = False
    if lista[i+1].type== 'i_objects':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta,i
def move_conditional(lista,i):
    respuesta = False
    if lista[i+1].type == 'cardinal':
        respuesta =True
        i+=1
    return respuesta,i
def zero_conditional(lista,i):
    respuesta = False
    if lista[i+1].type == 'number':
        respuesta =True
        i+=1
    return respuesta,i
def not_conditional(lista,i):
    respuesta = False
    a,i =cond(lista,i+1)
    if a == True:
        respuesta =True
    return respuesta,i

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
    return respuesta,i

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
    return respuesta,i
#command move
def ismove(token):
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
    return respuesta,i

    
#command skip
def isskip(token):
    """where n is a number or a variable or a constant. The robot
    should jump n steps forward."""
    if token.type =="skip":
        return True
    else:
        return False
def skip(lista,i):
    respuesta = False
    if lista[i+1].type == 'number':
        respuesta =True
        i+=1
    return respuesta,i
#command turn 
def isturn(token):
    """where D can be :left, :right, or :around (defined as constants).
    The robot should turn 90 degrees in the direction of the parameter in the
    first to cases, and 180 in the last case."""
    if token.type =="turn":
        return True
    else:
        return False
def turn(lista,i):
    respuesta = False
    if lista[i+1].type == 'direction':
        respuesta =True
        i+=1
    return respuesta,i




#command face 
def isface(token):
    """where O can be :north, :south, :east, or :west (all constants).
    The robot should turn so that it ends up facing direction O."""
    if token.type =="face":
        return True
    else:
        return False
    
def face(lista,i):
    respuesta = False
    if lista[i+1].type == 'cardinal':
        respuesta =True
        i+=1
    return respuesta,i
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
    if lista[i+1].type== 'i_objects':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta,i

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
    if lista[i+1].type== 'i_objects':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'number':
            respuesta =True
            i+=1
    return respuesta,i
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
    if lista[i+1].type== 'number':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'cardinal':
            respuesta =True
            i+=1
    return respuesta,i
#command run_dirs
def isrun_dirs(token):
    """where Ds is a non-empty list of directions: :front, :right,
    :left, :back. The robot should move in the directions indicated by the
    list and end up facing the same direction as it started."""
    if token.type =="run_dirs":
        return True
    else:
        return False
def run_dirs(lista,i):
    respuesta = False
    if lista[i+1].type == 'direction':
        respuesta =True
        i+=1
    return respuesta,i

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
    if lista[i+1].type== 'number':
        respuesta = True
        i+=1
        z=lista[i+1]
        if lista[i+1].type == 'cardinal':
            respuesta =True
            i+=1
    return respuesta,i
def isnull(token):
    if token.type =="null":
        return True
    else:
        return False
        

    
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
    

def function(lista, i):
    z = lista[i]
    f= lista[i+1]
    respuesta= False
    if iscommand(lista[i+1]) == True:
                    if lista[i+1].type == 'defvar' or lista[i+1].type=='equals' or lista[i+1].type == 'put' or lista[i+1].type == 'pick' or lista[i+1].type=="move_dir" or lista[i+1].type=="move_face":
                        if isdefvar(lista[i+1]) ==True:
                            respuesta,i =defvar(lista,i+1) 
                        if isequals(lista[i+1]) ==True:
                            respuesta,i= equals(lista,i+1) 
                        if isput(lista[i+1]) ==True:
                            respuesta,i =put(lista,i+1) 
                        if ispick(lista[i+1]) ==True:
                            respuesta,i =pick(lista,i+1) 
                        if ismove_dir(lista[i+1]) ==True:
                            respuesta,i =move_dir(lista,i+1)
                        if ismove_face(lista[i+1]) ==True:
                            respuesta,i=move_face(lista,i+1) 
                    else:
                        if ismove(lista[i+1]) ==True:
                            respuesta,i= move(lista,i+1) 
                        if isskip(lista[i+1]) ==True:
                            respuesta,i=skip(lista,i+1) 
                        if isturn(lista[i+1]) ==True:
                            respuesta,i= turn(lista,i+1) 
                        if isface(lista[i+1]) ==True:
                            respuesta,i= face(lista,i+1) 
                        if isrun_dirs(lista[i+1]) ==True:
                            respuesta,i=run_dirs(lista,i+1)
                        if isnull(lista[i+1]) ==True:
                            respuesta= True
    return respuesta,i

Defun ={}

def defun(lista,i):
    respuesta = False
    parentesis =0
    con =0
    if lista[i+1].type =="nombre":
            Defun[(lista[i+1]).value] =""
            i+=1
   
            if lista[i+1].type =="left_parenth":
                i+=1
                parentesis-=1
                
                a = lista[i+1].type == "nombre"
                while(lista[i+1].type == "nombre"):
                    con +=1
                    i+=1
                    Defun[(lista[i+1])]= con
                
                if lista[i+1].type == "right_parenth":
                    i+=1
                    parentesis-=1
                   


    return respuesta,i
            
def definida(lista,i):
    respuesta = False
    if len(Defun)==0:
        return respuesta
    else:
        for j in Defun:
            if j == lista[i].value:
                respuesta = True
                cont = lista[j]
                while(j<cont):
                    if lista[i+1].type=="Nombre":
                        repuesta = True
                    j+=1
