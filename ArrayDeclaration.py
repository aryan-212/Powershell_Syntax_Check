from ply import lex, yacc

# Lexer
tokens = ('IDENTIFIER', 'DOLLAR_SIGN', 'EQUALS', 'SEMICOLON', 'LBRACKET', 'RBRACKET', 'NUMBER', 'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'LPAREN', 'RPAREN')

t_DOLLAR_SIGN = r'\$'
t_EQUALS = r'='
t_SEMICOLON = r';'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIVIDE = r'/'
t_LPAREN = r'\('
t_RPAREN = r'\)'

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
    '''statement : variable_declaration
                 | array_declaration
                 | expression SEMICOLON'''

def p_variable_declaration(p):
    '''variable_declaration : DOLLAR_SIGN IDENTIFIER EQUALS expression SEMICOLON'''

    print(f"Variable Declaration: {p[2]}")

def p_array_declaration(p):
    '''array_declaration : DOLLAR_SIGN IDENTIFIER LBRACKET expression_opt RBRACKET EQUALS expression SEMICOLON'''

    print(f"Array Declaration: {p[2]}[{p[4]}]")

def p_expression_opt(p):
    '''expression_opt : expression
                     | empty'''

def p_expression(p):
    '''expression : term
                  | expression PLUS term
                  | expression MINUS term
                  | expression TIMES term
                  | expression DIVIDE term'''

def p_term(p):
    '''term : factor
            | term LBRACKET expression RBRACKET
            | term TIMES factor
            | term DIVIDE factor'''

def p_factor(p):
    '''factor : primary
              | factor MINUS primary'''

def p_primary(p):
    '''primary : IDENTIFIER
               | DOLLAR_SIGN IDENTIFIER
               | NUMBER
               | LPAREN expression RPAREN'''

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
parser = yacc.yacc()

# Test the parser
data = """
$array142[1]=246;
$another_array[1]=$array1[0];
$jsfhsk[90] = 89;
"""

lexer.input(data)
for tok in lexer:
    print(tok)

parser.parse(data)
