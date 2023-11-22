import ply.lex as lex
import ply.yacc as yacc

# Define the lexer for PowerShell comments
tokens = (
    'COMMENT',
)

# Define the regex for PowerShell comments
def t_COMMENT(t):
    r'\#.*'
    return t

# Ignore whitespace, including newlines
t_ignore = ' \t'

# Define how to handle newlines
def t_newline(t):
    r'\n+'
    t.lexer.lineno += len(t.value)

# Error handling
def t_error(t):
    print(f"Illegal character '{t.value[0]}'")
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex()

# Define the parser for PowerShell comments
def p_comment(p):
    'comment : COMMENT'
    pass

# Error handling in the parser
def p_error(p):
    print(f"Syntax error at '{p.value}'")

# Build the parser
parser = yacc.yacc()

# Test the syntax validation
if __name__ == "__main__":
    input_string = """
    #This is a valid comment
    #Another comment
    Not a comment
    """
    
    lexer.input(input_string)
    
    while True:
        tok = lexer.token()
        if not tok:
            break
        print(tok)

    parser.parse(input_string)
