from arpeggio import RegExMatch, Optional, ZeroOrMore, OneOrMore, EOF

##############
#Math Portion#
##############

#Int or float or nothing
def number():
    return [RegExMatch('\d*\.\d*|\d+'), RegExMatch('\w+')]

#An optional plus/minus followed by a number or an arithmetic expression
def factor():
    return Optional(["+", "-"]), [number, ("(", arithmetic_expression, ")")]

#One or more factors multiplied/divided together
def mult_term():
    return factor, ZeroOrMore(["*", "/"], factor)
    
#One or more terms added/subtracted together
def arithmetic_expression():
    return mult_term, ZeroOrMore(["+", "-"], mult_term)

####################
#Built in Functions#
####################

#Handles varaible assignment
def var_decl():
    return RegExMatch('\w+'), "=", evaluatable

#Handles variable declaration
def let():
    return "let", [var_decl, RegExMatch('\w+')], ZeroOrMore(",", [var_decl, RegExMatch('\w+')])

#Handles boolean expressions ==, !=, >=, >, <=, <
def boolean_expression():
    return [(arithmetic_expression, ["==", "!=", ">=", ">", "<=", "<"], arithmetic_expression), "0", "1"]

#Handles a print statement
def print_func():
    return "print(", func_parameters, ")"

#Handles code blocks statements
def code_block():
    return "{", ZeroOrMore(valid_line), "}"
    
#Handles if statements
def if_statement():
    return "if", boolean_expression, code_block, "else", code_block

#########################
#Non-Interpretable types#
#########################

#Declares what types can be their own line
def valid_line():
    return [if_statement, print_func, let, var_decl, arithmetic_expression]

#Declares what types can be evaluated to a value
def evaluatable():
    return [if_statement, code_block, boolean_expression, arithmetic_expression, RegExMatch('\w+')]
    
#Declares format of function parameters
def func_parameters():
    return Optional(evaluatable), ZeroOrMore(",", [evaluatable])

#######################
#Interpreter Interface#
#######################

#Commenting format to pass into Arpeggio.ParserPython
def comment():
    return RegExMatch('#.*')

#Top level of the grammar
def code():
    return ZeroOrMore(valid_line), EOF