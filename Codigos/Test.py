# Equipo 
# Billy Diaz de Luis
# Maribel Montoya Hernandez
# Ana Laura Lopez Martinez

import sys
from AnalizadorLexico import lexer

if __name__ == "__main__":
    file_name = sys.argv[1]
    f = open(file_name, "r")

    data = f.read()
    lexer.input(data)
    f1 = open ('salidaLETIF.txt','w')

    while True:
        tok = lexer.token()
        if not tok:
            break
        print("Token-->",tok)
        f1.write("Token-->" + str(tok))
    f1.close()
    

