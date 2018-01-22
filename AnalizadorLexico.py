import ply.lex as lex
import re
import codecs
import os
import sys

tokens=['ID','NUMERO','CADENA_CARACTERES','PLUS','MAYOR','MENOR','NEGACION','PARENTESIS_AB','PARENTESIS_CE',
'CONSTANTE_ENTERA','DISTINTO','COMENTARIOS','AND','AUTO_DECREMENTO','PUNTO','COMA','PUNTO_Y_COMA','MENOS',
'ASIGNACION','LLAVE_ABIERTA','LLAVE_CERRADA','DOS_PUNTOS','AUTO_INC','AUTO_DEC','TIPO']

reservadas={'while':'WHILE', 'if':'IF','write':'WRITE','var':'VAR', 'prompt' :'PROMPT', 'function' :'FUNCTION','return' : 'RETURN', 'prompt':'PROMPT', 'write':'WRITE','int':'INT','chars':'CHARS','bool':'BOOL'}


tokens=tokens+list(reservadas.values())


t_PLUS = r'\+'
t_MENOS = r'\-'
t_ASIGNACION = r'\='
t_PUNTO = r'\.'
t_PUNTO_Y_COMA = r'\;'
t_COMA = r'\,'
t_AND = r'\&'
t_MAYOR = r'\>'
t_MENOR = r'\<'
t_NEGACION = r'\!'
t_LLAVE_ABIERTA = r'\{'
t_LLAVE_CERRADA = r'\}'
t_PARENTESIS_AB = r'\('
t_PARENTESIS_CE = r'\)'
t_DOS_PUNTOS = r':'
t_AUTO_INC = r'\+\+'
t_AUTO_DEC = r'\-\-'


def t_newline(t):
	r'\n+'
	t.lexer.lineno += len(t.value)

def t_ID(t):
        r'[a-zA-Z_][a-zA-Z0-9_]*'
        if t.value.lower() in reservadas:
            t.value = t.value.upper()
            t.type = t.value
        return t

def t_CADENA_CARACTERES(t):
        r'["a-zA-Z_][a-zA-Z_"]*'
        return t


def t_NUMERO(t):
        r'\d+'
        t.value =int(t.value)
        return t
            

def t_COMENTARIOS(t):
    r'\\.*'
    pass

def t_saltoLinea(t):
    r'\n+'
    t.lexer.lineno +=len(t.value)  
    

def t_error(t):
    print("caracter no valido '%s' " % t.value[0])
    t.lexer.skip(1)


tokenizar=lex.lex()
f1=open("prueba/Prueba.txt",'r')
cadenaFichero = f1.read()
print cadenaFichero
tokenizar.input(cadenaFichero)
while True:
    to=tokenizar.token()    
    if not to:
        print "Error: "
        print to
        break
    print to
