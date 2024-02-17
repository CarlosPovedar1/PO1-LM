import ply.lex as lex
import commands as cd




tokens = ["nombre", "move", "skip", "turn", "face", "put",
           "pick", "move_dir", "run_dirs", "move_face", "null", "conditional",
           "loop", "repeat", "defun", "fun_call", "left_parenth", "right_parenth", "variable", "number", "if", "defvar", "cardinal", "direction", "comma", "i_objects"]



"""
for linea in archivo:
                # Elimina los espacios en blanco al principio y al final de la línea
                linea = linea.strip()
                print(linea)"""


    


def t_defvar(t):
    r'defvar'
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

def t_conditional(t):
    r'facing\?|blocked\?|can-put\?|can-move\?|isZero\?|not'
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

t_ignore = ' \t'


def print_menu():
    print("Bienvenido")
    print("1- Cargar archivo txt")
    print("0- Salir")

working = True
while working:
    print_menu()
    inputs = input('Seleccione una opción para continuar\n')
    if int(inputs) == 1:
        file = str(input('digite el archivo sin txt: '))
        with open(f'{file}.txt', 'r') as archivo:
            
            lexer = lex.lex()
            for linea in archivo:
                lexer.input(linea)
                while True:
                    tok = lexer.token()
                    if not tok:
                        break  # No more input
                    print(tok)
    elif int(inputs) ==0:
            working= False

"""lexer = lex.lex()
data = "(defun goend() (if (not (blocked?)) ((pick :balloons 5) (goend))(null)))"
lexer.input(data)
while True:
    tok = lexer.token()
    if not tok:
        break  # No more input
    print(tok)
"""


