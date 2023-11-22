from ply import lex, yacc

# Lexer
tokens = ('IDENTIFIER', 'DOLLAR_SIGN', 'EQUALS', 'SEMICOLON', 'OPERATOR', 'NUMBER')

t_DOLLAR_SIGN = r'\$'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_OPERATOR = r'[\+\-\*/]'

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.value = t.value  # Store the value for later use
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
    '''program : statement
               | program statement'''

def p_statement(p):
    '''statement : DOLLAR_SIGN IDENTIFIER EQUALS expression SEMICOLON
                 | expression SEMICOLON'''

    if len(p) == 6:
        print(f"Variable Declaration: {p[2]}")

def p_expression(p):
    '''expression : IDENTIFIER
                  | DOLLAR_SIGN IDENTIFIER
                  | NUMBER
                  | expression OPERATOR expression'''

    if len(p) == 4:
        print(f"Binary Operation: {p[1]} {p[2]} {p[3]}")

def p_error(p):
    if p:
        print(f"Syntax error at line {p.lineno}, position {find_column(p.lexer.lexdata, p)}: Unexpected token '{p.value}'")
    else:
        print("Syntax error at EOF")

precedence = (
    ('left', 'OPERATOR'),
)

lexer = lex.lex()
parser = yacc.yacc()

# Test the parser
data = """
$variable1 = 42;
another_variable  $variable1 / 10 * 2;
"""

lexer.input(data)
for tok in lexer:
    print(tok)

parser.parse(data)
