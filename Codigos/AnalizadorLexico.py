# Equipo 
# Billy Diaz de Luis
# Maribel Montoya Hernandez
# Ana Laura Lopez Martinez


import ply.lex as lex

#1) Lista de palabras reservadas
#inicio reserved Maribel
reserved = {
    'let' : 'LET',
    'in' : 'IN' ,
    'endlet' : 'ENDLET',
    'if' : 'IF' ,
    'then' : 'THEN',
    'else' : 'ELSE' ,
    'endif':'ENDIF'
    }
#termina reserved Maribel

# 2) Lista de tokens
tokens = [
    'PTCOMA',
    'PARIZQ',
    'PARDER',
    'DECIMAL',
    'ENTERO',
    'INCREMENTO',  #Se ordenan de mayor longitud a menor si coincide un caracter, por ejem, '+=' e '+'
    'MAS',
    'COMENTARIO',
    'IDENTIFICADOR',

    #Inicia tokens Billy
    'MENOS',
    'ASIGNACION',
    'MULTIPLICACION',
    'DIVISION',
    'MAYORQ',
    'MENORQ',
    'MAYORIGUAL',
    'MENORIGUAL',
    'IGUAL',
    'DIFERENTE'
    #Termina tokens Billy

    
] + list(reserved.values())

# 3) Especificación de los tokens

#A) Tokens simples, que solo se definen mediante expresiones regulares
# Inician con el prefijo "t_" seguido del nombre del Token

#inicio reservada Maribel
#Se incluyen uno por cada palabra reservada
t_LET = r'let'
t_IN = r'in'
t_ENDLET = r'endlet'
t_IF = r'if'
t_THEN = r'then'
t_ELSE = r'else'
t_ENDIF = r'endif'
#termino reservada Maribel


t_PTCOMA     = r';'  
t_PARIZQ    = r'\('
t_PARDER    = r'\)'
t_INCREMENTO = r'\+='
t_MAS       = r'\+'
t_ignore = " \t" #caracteres ignorados: espacio y tabulador

#Inician tokens simples Billy
t_MENOS = r'\-'
t_ASIGNACION= r'\='
t_MULTIPLICACION= r'\*'
t_DIVISION= r'\/'
t_MAYORQ= r'\>'
t_MENORQ= r'\<'
t_MAYORIGUAL= r'\>='
t_MENORIGUAL= r'\<='
t_IGUAL= r'\=='
t_DIFERENTE= r'\!='
#Termina tokens simples billy


#B) Tokens que requieren una acción
# Las definiciones de Tokens que requieren otros tipo de acciones se realizan mediante Funciones
# El argumento t es una instancia de LexerToken, el cual tiene cuatro atributos:
# t.type -> tipo del token (int, string, ..)
# t.value -> es el lexema
# t.lineno -> línea en la que se encontró
# t.lexpos -> posición relativa al inicio del texto


def t_DECIMAL(t):
    r'\d+\.\d+' #El punto se tiene que escapar porque en expresiones regulares significa cualqueir símbolo
    try:
        t.value = float(t.value) 
    except ValueError:
        print("El valor flotante excede los límites %f", t.value)
        t.value = 0
    return t #Siempre se debe devolver el objeto t, de lo contrario se descarta el token


def t_ENTERO(t):
    r'\d+'  #\d es equivalente a [0-9]
    try:
        t.value = int(t.value)
    except ValueError:
        print("El valor entero excede los límites %d", t.value)
        t.value = 0
    return t #Siempre se debe devolver el objeto t, de lo contrario se descarta el token


def t_IDENTIFICADOR(t):
    r'[a-z|_] [a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'IDENTIFICADOR')
    return t

def t_COMENTARIO(t):
    r'%.*' # Una línea que inicia con '#', seguida de lo que una cadena conformada por cualesqueira símbolos
    pass
    # No regresa ningún valor. El token es ignorado
    
    

#Definir una regla para que podamos rastrear los números de línea.
def t_newline(t):
    r'\n+'   #expresión regular para indicar que es uno o más saltos de línea
    t.lexer.lineno += len(t.value) 
    

#Definir una regla para los caracteres inválidos
def t_error(t):
    print("Caracter ilegal '%s'" % t.value[0])
    t.lexer.skip(1) #se salta un caracter 


#Construimos el lexer 
lexer = lex.lex()



