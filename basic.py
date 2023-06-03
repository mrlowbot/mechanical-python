######################################
# TOKENS: mechanical-python
# Hyper construction of advanced algorithms in combination of several different algorithms => https://www.youtube.com/watch?v=xvFZjo5PgG0
######################################

TT_INT  = 'TT_INT'
TT_FLOAT = 'TT_FLOAT'
TT_PLUS = 'TT_PLUS'
TT_MINUS = 'TT_MINUS'
TT_MUL = 'TT_MUL'
TT_DIV = 'TT_DIV'
TT_LPAREN = 'TT_LPAREN'
TT_RPAREN = 'TT_RPAREN'


class Token:
    def __init__(self, type_, value):
        self.type = type_
        self.value = value
        
    def __repr__(self):
        if self.value: return f'{self.type}:{self.value}'
        return f'{self.type}'
    
    
######################################
# LEXER: mechanical-python
######################################

class Lexer:
    def __init__(self, text):
        self.text = text
        self.pos = -1
        self.current_char = None