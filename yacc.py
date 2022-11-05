import ply.yacc as yacc

from lex import lexico
from teste import arquivo_de_teste

tokens = lexico.tokens


def p_declaracao(p):
    '''declaracao : variavel
                  | variavel declaracao'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]


def p_variavel(p):
    '''variavel : tipo identificador finalizador'''
    p[0] = p[1] + " " + p[2] + p[3]


def p_tipo(p):
    '''tipo : CHAR
            | FLOAT
            | INT'''
    p[0] = p[1]


def p_identificador(p):
    '''identificador : ID
                     | ID separador'''
    if len(p) == 2:
        p[0] = p[1]
    elif len(p) == 3:
        p[0] = p[1] + p[2]


def p_separador(p):
    '''separador : VIRGULA identificador'''
    p[0] = p[1] + p[2]


def p_finalizador(p):
    'finalizador : PONTO_E_VIRGULA'
    p[0] = p[1] + '\n'


def p_error(p):
    print(f'Syntax error in input!\n(Erro, valor: {p.value}, linha: {p.lineno})')


# Build the parser
parser = yacc.yacc()

s = arquivo_de_teste()
result = parser.parse(s)

print(result)
