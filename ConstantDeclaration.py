from ply import lex, yacc

# Lexer
tokens = ('IDENTIFIER', 'DOLLAR_SIGN', 'EQUALS', 'SEMICOLON', 'NUMBER', 'CONST')

t_EQUALS = r'='
t_SEMICOLON = r';'
t_DOLLAR_SIGN = r'\$'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'CONST' if t.value == 'const' else 'IDENTIFIER'
    return t

def t_NUMBER(t):
    r'\d+'
    t.value = int(t.value)
    return t

t_ignore = ' \t\n'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Parser
def p_program(p):
    '''program : const_declaration
               | empty'''

def p_const_declaration(p):
    '''const_declaration : CONST DOLLAR_SIGN IDENTIFIER EQUALS NUMBER SEMICOLON'''
    print(f"Constant Declaration: {p[3]} = {p[5]}")

def p_empty(p):
    'empty :'
    pass

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {find_column(p.lexer.lexdata, p)}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

def find_column(input, token):
    last_cr = input.rfind('\n', 0, token.lexpos)
    if last_cr < 0:
        last_cr = 0
    column = (token.lexpos - last_cr) + 1
    return column

lexer = lex.lex()
parser = yacc.yacc(debug=True)

# Test the parser
data = """
const $myconstant = -52;
"""

lexer.input(data)
for tok in lexer:
    print(tok)

parser.parse(data)
