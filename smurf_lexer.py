from rply import LexerGenerator

class Lexer():
    def __init__(self):
        self.lexer = LexerGenerator()

    def add_tokens(self):
        # let
        self.lexer.add('LET', r'let')

        # print
        self.lexer.add('PRINT', r'print')

        # parenthesis
        self.lexer.add('OPEN_PAREN', r'\(')
        self.lexer.add('CLOSE_PAREN', r'\)')

        # operators
        self.lexer.add('SUM', r'\+')
        self.lexer.add('SUB', r'\-')
        self.lexer.add('MULT', r'\*')
        self.lexer.add('DIV', r'\/')
        self.lexer.add('ASSIGN', r'\=')

        # number
        self.lexer.add('NUMBER', r'\d+')

        # variable
        self.lexer.add('VAR', r'\w')

        # comma
        self.lexer.add('COMMA', r'\,')

        # ignore spaces
        self.lexer.ignore(r'\s+')

        # ignore comments
        self.lexer.ignore(r'\#.*')

    def get_lexer(self):
        self.add_tokens()
        return self.lexer.build()