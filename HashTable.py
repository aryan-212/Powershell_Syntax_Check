from ply import lex, yacc

# Lexer
tokens = ('DOLLAR_SIGN', 'IDENTIFIER', 'AT', 'LBRACE', 'RBRACE', 'STRING', 'COMMA', 'NEWLINE', 'SEMICOLON', 'EQUALS')

t_DOLLAR_SIGN = r'\$'
t_AT = r'@'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_COMMA = r','
t_SEMICOLON = r';'
t_EQUALS = r'='

def t_STRING(t):
    r'"[^"]*"'
    return t

def t_NEWLINE(t):
    r'\n+'
    t.lexer.lineno += t.value.count('\n')

def t_IDENTIFIER(t):
    r'[a-zA-Z_][a-zA-Z0-9_]*'
    t.type = 'IDENTIFIER'
    return t

t_ignore = ' \t'

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Parser
def p_program(p):
    '''program : hash_table
               | program NEWLINE'''

def p_hash_table(p):
    '''hash_table : DOLLAR_SIGN IDENTIFIER EQUALS AT LBRACE hash_entries RBRACE SEMICOLON'''

    print(f"Hash Table Declaration: {p[2]}")

def p_hash_entries(p):
    '''hash_entries : hash_entry COMMA hash_entry
                    | hash_entries NEWLINE'''

def p_hash_entry(p):
    '''hash_entry : IDENTIFIER EQUALS STRING
                  | IDENTIFIER'''

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
$AryAn = @{
    Key1 = " ",
    Key2 = "Value2"
;
"""

lexer.input(data)
for tok in lexer:
    print(tok)

parser.parse(data)
