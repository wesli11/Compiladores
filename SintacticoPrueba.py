import ply.yacc as yacc
import os
import re
import codecs
from AnalizadorLexico import tokens
from sys import stdin

precedence = (
        ('right','ID','IF','WHILE'),
        ('right','VAR'),
        ('rigth', 'ASIGNACION'),
        ('left','DISTINTO'),
        ('left','MAYOR','MENOR'),
        ('left','PLUS'),
        ('left','PARENTESIS_AB','PARENTESIS_CE'),
        ('left','LLAVE_ABIERTA','LLAVE_CERRADA')
        )

# NO TERMINALES=NOMBRES DE NUESTRAS FUNCIONES
# TERMINALES=NUESTROS TOKENS DEL AL
def p_program(p):
        '''program : block'''
        print "program"
	    #p[0] = program(p[1],"program")

def p_block(p):
      	'''block : D_de decFun Sprima empty'''
        #p[0] = block(p[1],p[2],p[3],"block")
	    print "block"

def p_varDeclSen1(p):
	    '''D_de :  VAR t_tipos ID j_J PUNTO_Y_COMA'''
	    #p[0] = varDeclSen1(tipo(p[2]),Id(p[3]),p[4],"varDeclSen1")
	    print "declaracion VAR"	

def pvarDelSen2(p):
        '''D_de : Sprima'''
        print "Sprima"     

def p_J1(p):
        '''j_J : COMA ID j_J'''
        #p[0] = J1(Id(p[2]),p[3],"J1")
        print "Jota 1"

def p_J2(p):
        '''j_J : empty'''
        #p[0] = Null()
        print "nulo"

def p_varDecl1(p):
	    '''a_A : t_tipos ID COMA a_A'''
	    #p[0] = varDecl1(tipo(p[1]),Id(p[2]),p[3],"varDecl1")
	    print "varDecSen 1"

def p_varDecl2(p):
	    '''a_A : t_tipos ID'''
	    #p[0] = varDecl2(tipo(p[1]),ID(p[2]),"varDecl2")
	    print "varDecSen 2"	

def p_varDecl4(p):
	    '''a_A : t_tipos ID PUNTO_Y_COMA'''
	    #p[0] = varDecl2(tipo(p[1]),ID(p[2]),"varDecl2")
	    print "varDecSen 3"        

def p_varDecl3(p):
	    '''a_A : empty'''
	    #p[0] = Null()
        print "nulo"	

def p_decfun1(p):
     	'''decFun : FUNCTION decTipos ID PARENTESIS_AB a_A PARENTESIS_CE LLAVE_ABIERTA Sprima LLAVE_CERRADA'''	
        #p[0] = decfun1((p[2]),Id(p[3]),p[5],"decfun1")
        print "decFun 1"  

	
def p_decTipos1(p):
	    '''decTipos : t_tipos'''
        #p[0] = decTipos1((p[1]),"decTipos1")
	    print "decTipos 1"   

def p_decTipos2(p):
	    '''decTipos : empty'''
	    #p[0] = Null()
        print "nulo" 


def p_Sprima1(p):
        '''Sprima : WHILE PARENTESIS_AB E PARENTESIS_CE LLAVE_ABIERTA sesese LLAVE_CERRADA'''
        #p[0] = Sprima1(E(p[3]),"while")
        print "Sprima whileEEEE"

def p_Sprima2(p):
        '''Sprima : sesese'''
        #p[0] = Sprima2(S_ese(p[1]),"Sprima2")
        print "Sprima 2"

def p_S1(p):
        '''sesese : ID ASIGNACION E PUNTO_Y_COMA'''
        #p[0] = S1(Id(p[1]),asig(p[2]),p[3],"S1")
        print "S_ese 1"

def p_Sinic(p):
        '''sesese : ID ASIGNACION E'''
        #p[0] = S1(Id(p[1]),asig(p[2]),p[3],"S1")
        print "S_ese 1"        

def p_S2(p):
        '''sesese : IF PARENTESIS_AB E PARENTESIS_CE'''
        #p[0] = S2((p[3]),"if condicional")
        print "if de ese"

def p_S3(p):
        '''sesese : RETURN E PUNTO_Y_COMA'''
        #p[0] = S3((p[2]),"return")
        print "return <<"

def p_S4(p):
        '''sesese : WRITE PARENTESIS_AB B PARENTESIS_CE PUNTO_Y_COMA'''
        #p[0] = S4(p[3],"write")
        print "write"

def p_S5(p):
        '''sesese : PROMPT PARENTESIS_AB ID PARENTESIS_CE PUNTO_Y_COMA'''
        #p[0] = S4(ID(p[3]),"PROMPT")
        print "S_ese 5"

def p_E1(p):
        '''E : E PLUS variable'''
        #p[0] = E1(p[1],(p[3]),"E1")
        print "E plus"
   
def p_E2(p):
        '''E : E MENOS variable'''
        #p[0] = E2(p[1],(p[3]),"E2")
        print "E menos"

def p_Emenor(p):
        '''E : E MENOR variable'''
        #p[0] = Emenor(p[1],(p[3]),"E1")
        print "menor <"

def p_Emayor(p):
        '''E : E MAYOR variable'''
        #p[0] = Emayor(p[1],(p[3]),"E1")
        print "E mayor"        

def p_variable1(p):
        '''variable : ID'''
        print "variable 1"

def p_numbero1(p):
	    '''variable : NUMERO'''
	    print "numero <<"   

def p_E3(p):
        '''E : variable'''
        #p[0] = E3(p[1],"E3")
        print "variab"
     
def p_E4(p):
        '''t_tipos : t_tipos AND Y'''
        #p[0] = E4(p[1],p[3],"and")
        print "T and"

def p_Y1(p):
        '''Y : E'''
        #p[0] = Y1(p[1],"Y1")
        print "E y"

def p_Y2(p):
        '''Y : E COMA Y'''
        #p[0] = Y2(p[1],p[3],"E3")
        print "E2"

def p_Y3(p):
        '''Y : empty'''
        #p[0] = Null()
        print "nulo"	

def p_Y4(p):
        '''Y : AUTO_INC Yprima'''
        #p[0] = Y4(p[2],"autoincremento")
        print "Y autoincremento"


def p_Y5(p):
        '''Yprima : ID'''
        #p[0] = Y2(ID(p[1]),"identif")
        print "Yprima identificador"

def p_Y6(p):
        '''Yprima : ID PARENTESIS_AB B PARENTESIS_CE'''
        #p[0] = Y6(ID(p[1]),p[3],"Y6")
        print "Yprima llamada a funcion"

def p_B1(p):
        '''B : E '''
        #p[0] = B1(p[1]),"B1")
        print "llamada a E"

def p_B2(p):
        '''B : E COMA B'''
        #p[0] = B2(p[1]),p[3],"B2")
        print " llamada B2"

def p_B3(p):
        '''B : empty'''
        #p[0] = Null()
        print "nulo"

def p_empty(p):
	    '''empty :'''
	    pass
	#pass ignora todo lo que hay en esa linea (vacio)


def p_decT1(p):
        '''t_tipos : INT'''
        #p[0] = decT1(int(p[1]),"entero")
     	print "entero"

def p_decT2(p):
        '''t_tipos : BOOL'''
        #p[0] = decT2(bool(p[1]),"booleano")
        print "booleano"

def p_decT3(p):
        '''t_tipos : CHARS'''
        #p[0] = decT3(caracter(p[1]),"caracter")
        print "caracter"

def p_error(p):
	    print "Error de sintaxis ", p
	    #print "Error en la linea "+str(p.lineno)

#tokenizar=lex.lex()
f1=open("prueba/Prueba.txt",'r')
cadenaFichero = f1.read()
print cadenaFichero
#tokenizar.input(cadenaFichero)
parser = yacc.yacc()
result = parser.parse(cadenaFichero)
print result
#yacc permite al programa hacer un analisis sintactico de todo el codigo fuente que le pasamos