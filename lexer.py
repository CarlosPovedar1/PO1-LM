import ply.lex as lex
import commands as cd




tokens = ["not_conditional","nombre", "move", "skip", "turn", "face", "put",
           "pick", "move_dir", "run_dirs", "move_face", "null", 
           "loop", "repeat", "defun", "fun_call", "left_parenth", "right_parenth",
            "variable", "number", "if", "defvar", "cardinal", "direction", "comma", "i_objects","equals",
            "facing_conditional","blocked_conditional","put_conditional","pick_conditional","move_conditional",
            "zero_conditional" ]


def t_facing_conditional(t):
    r'facing\?'
    return t
def t_blocked_conditional(t):
    r'blocked\?'
    return t
def t_put_conditional(t):
    r'can-put\?'
    return t
def t_move_conditional(t):
    r'can-move\?'
    return t
def t_pick_conditional(t):
    r'can-pick\?'
    return t
def t_zero_conditional(t):
    r'isZero\?'
    return t
def t_not_conditional(t):
    r'not'
    return t



def t_defvar(t):
    r'defvar'
    return t
def t_equals(t):
    r'equals'
    return t

def t_run_dirs(t):
    r'run-dirs'
    return t

def t_move_dir(t):
    r'move-dir'
    return t

def t_move(t):
    r'move'
    return t

def t_skip(t):
    r'skip'
    return t

def t_null(t):
    r'null'
    return t

def t_turn(t):
    r'turn'
    return t

def t_face(t):
    r'face'
    return t

def t_put(t):
    r'put'
    return t

def t_pick(t):
    r'pick'
    return t

def t_move_face(t):
    r'move-face'
    return t

def t_if(t):
    r'if'
    return t

def t_loop(t):
    r'loop'
    return t

def t_repeat(t):
    r'repeat'
    return t

def t_defun(t):
    r'defun'
    return t

def t_left_parenth(t):
    r'\('
    return t

def t_right_parenth(t):
    r'\)'
    return t

def t_number(t):
    r'\d+'
    return t


def t_cardinal(t):
    r':north|:west|:south|:east'
    return t
    
def t_direction(t):
    r':left|:right|:around'
    return t

def t_comma(t):
    r','
    return t

def t_i_objects(t):
    r':chips|:balloons'
    return t

def t_nombre(t):
    r'[a-zA-Z_][a-zA-z0-9_]*'
    return t

def t_error(t):
    print("Carácter ilegal: '%s'" % t.value[0])
    t.lexer.skip(1)

t_ignore = ' \t|\n'

Defun ={}

def print_menu():
    print("Bienvenido")
    print("1- Cargar archivo txt")
    print("0- Salir")
respuesta = False
working = True
while working:
    print_menu()
    inputs = input('Seleccione una opción para continuar\n')
    work = True
    lista= []
    if int(inputs) == 1:
        file = str(input('digite el archivo sin txt: '))
        with open(f'{file}.txt', 'r') as archivo:
        
            
            for linea in archivo:
                lexer = lex.lex()
                lexer.input(linea)
                while True:
                    tok = lexer.token()
                    if not tok:
                        break 
                    lista.append(tok)   
                
                #contador de parentesis
            contador =0
            i =0
            
            while work and i< len(lista):
                """if not tok:
                    respuesta = False
                    break """ # No more input 
                z=lista[i]
                if lista[i].type == 'left_parenth':
                        contador -=1
                       
                elif lista[i].type == 'right_parenth':
                        contador +=1
                   
                #commandos
                elif cd.iscommand(lista[i]) == True:
                    respuesta = False
                    if lista[i].type == 'defvar' or lista[i].type=='equals' or lista[i].type == 'put' or lista[i].type == 'pick' or lista[i].type=="move_dir" or lista[i].type=="move_face":
                        if cd.isdefvar(lista[i]) ==True:
                            respuesta,i =cd.defvar(lista,i) 
                        if cd.isequals(lista[i]) ==True:
                            respuesta,i= cd.equals(lista,i) 
                        if cd.isput(lista[i]) ==True:
                            respuesta,i =cd.put(lista,i) 
                        if cd.ispick(lista[i]) ==True:
                            respuesta,i =cd.pick(lista,i) 
                        if cd.ismove_dir(lista[i]) ==True:
                            respuesta,i =cd.move_dir(lista,i)
                        if cd.ismove_face(lista[i]) ==True:
                            respuesta,i=cd.move_face(lista,i) 
                    else:
                        if cd.ismove(lista[i]) ==True:
                            respuesta,i= cd.move(lista,i) 
                        if cd.isskip(lista[i]) ==True:
                            respuesta,i=cd.skip(lista,i) 
                        if cd.isturn(lista[i]) ==True:
                            respuesta,i= cd.turn(lista,i) 
                        if cd.isface(lista[i]) ==True:
                            respuesta,i= cd.face(lista,i) 
                        if cd.isrun_dirs(lista[i]) ==True:
                            respuesta,i=cd.run_dirs(lista,i)
                        if cd.isnull(lista[i]) ==True:
                            respuesta= True
                        


                #conditional
                
                elif cd.Conditional(lista[i]) ==True:
                        if  lista[i+1].type == 'left_parenth':
                            contador-=1
                            i+=1
                        
                        r,i = cd.cond(lista,i+1)
                        if r==True:
                            if lista[i+1].type =='right_parenth':
                                contador+=1
                                i+=1
                            if lista[i+1].type == 'left_parenth':
                                contador-=1
                                i+=1
                                z,i = cd.function(lista,i)
                                if z==True:
                                    if lista[i+1].type =='right_parenth':
                                        contador+=1
                                        i+=1
                                    if lista[i+1].type == 'left_parenth':
                                        contador-=1
                                        i+=1
                                        f= lista[i]
                                        z,i = cd.function(lista,i)
                                        if cd.function(lista,i+1)==True :
                                            if lista[i+1].type =='right_parenth':
                                                contador+=1
                                                i+=1
                                            if lista[i+1].type == 'left_parenth':
                                                contador-=1
                                                i+=1
                                        elif cd.isnull(lista[i+1]):
                                            i+=1
                                            if lista[i+1].type =='right_parenth':
                                                contador+=1
                                                i+=1
                                            if lista[i+1].type =='right_parenth':
                                                contador+=1
                                                i+=1
                                          
                        else:
                            respuesta =False
                elif lista[i].type =="defun": 
                    respuesta,i,Defun = cd.defun(lista,i)      
                                
                elif len(Defun) >= 0:
                    for j in Defun:
                        f = lista[i+1]
                        x = lista[i].value
                        if lista[i].value == j:
                            respuesta,i = cd.definida(lista,i)
                elif lista[i].type =="repeat":
                    cd.Repeat(lista,i)    
                elif lista[i].type =="loop":
                    cd.loop(lista,i) 
                        

                
                    
                i+=1
            if contador ==0 and respuesta ==True:
                print("--------Yes--------")
            else:
                print("---------No-----------")
        
          
    elif int(inputs) ==0:
            working= False




