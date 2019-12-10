from arpeggio import RegExMatch, Optional, ZeroOrMore, OneOrMore, EOF


#integer = "-"? [0-9]+
def integer():
    return [RegExMatch('\d*\.\d'), RegExMatch('\d+')]

#addop   = '+' | '-'
#mulop   = '*' | '/'
#relop   = '==' | '!=' | '>=' | '>' | '<=' | '<'


def mulop():
    return ['*','/']

def addop():
    return ['+', '-']

def relop():
    return ['==', '!=', '>=', '>', '<=', '<']

#mult_term  = primary mulop mult_term | primary
#arithmetic_expression  = mult_term addop arithmetic_expression | mult_term
#boolean_expression  = arithmetic_expression relop arithmetic_expression


def mult_term():
    return [(primary, mulop, mult_term), primary]


def arithmetic_expression():
    return [(mult_term, addop, arithmetic_expression), mult_term]

def boolean_expression():
    return arithmetic_expression, relop, arithmetic_expression


#identifier = [a-z][a-zA-Z_0-9]*
#variable_reference = identifier
#expr  = "fn" function_definition | "if" if_expression | boolean_expression | arithmetic_expression
#assignment  = identifier "=" expr


def identifier():
    return OneOrMore(RegExMatch('[a-z][a-zA-Z_0-9]*'))

def variable_reference():
    return identifier

def assignment():
    return identifier, "=", expr

def expr():
    return [("if", if_expression), boolean_expression, arithmetic_expression]


#decl = identifier ("=" expr)?
#variable_declaration  = decl ("," decl)*
#primary  = integer | function_call | variable_reference | "(" arithmetic_expression ")"


def decl():
    return identifier, Optional("=", [integer, identifier])

def variable_declaration():
    return decl, ZeroOrMore(",", decl)

def primary():
    return [integer, function_call, variable_reference, ( "(", arithmetic_expression, ")")]

#statement = "let" variable_declaration | assignment | expr
#comment  = "#" r'.*'
#brace_block = "{" code  "}"
#print = print, "(", identifier, ")"


def statement():
    return [("let", variable_declaration), assignment, expr, print_smurf]

def comment():
    return RegExMatch('#.*')

def brace_block():
    return "{", code, "}"

def print_smurf():
    return "print", "(", [arithmetic_expression, boolean_expression, identifier], ")"

def call_arguments():
    return (expr, ZeroOrMore(",", expr))

def function_call():
    return [(variable_reference, "(", call_arguments, ")"), ("print", "(", call_arguments, ")")]

def param_list():
    return [("(", identifier, ZeroOrMore(",", identifier), ")" ), "()"]

def function_definition():
    return param_list, brace_block

#if_expression = expr brace_block ( "else" brace_block )?
def if_expression():
    return expr, brace_block, Optional("else", brace_block)

#code = statement*
def code():
    return ZeroOrMore(statement)

#program = code EOF
def program():
    return code, EOF
