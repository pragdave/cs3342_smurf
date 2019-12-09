from arpeggio import RegExMatch, Optional, ZeroOrMore, OneOrMore, EOF

##############
#Math Portion#
##############

#Int or float or nothing
def number():
    return Optional("-"), RegExMatch('\d*\.\d*|\d+')
    
def var_ref():
    return RegExMatch('[a-z][a-zA-Z_0-9]*')
    
#An optional plus/minus followed by a number or an arithmetic expression
def factor():
    return [number, fn_call, var_ref, ("(", arithmetic_expression, ")")]

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
    return var_ref, "=", evaluatable

#Handles variable declaration
def var_let():
    return "let", [var_decl, var_ref], ZeroOrMore(",", [var_decl, var_ref])

#Handles boolean expressions ==, !=, >=, >, <=, <
def boolean_expression():
    return [(arithmetic_expression, ["==", "!=", ">=", ">", "<=", "<"], arithmetic_expression), "0", "1"]

#Handles a print statement
def print_func():
    return "print", func_parameters

#Handles code blocks statements
def code_block():
    return "{", ZeroOrMore(valid_line), "}"
    
#Handles if statements
def if_statement():
    return "if", boolean_expression, code_block, "else", code_block
    
#Handles function assignment
def fn_decl():
    return var_ref, "=", "fn", "(", Optional(var_ref), ZeroOrMore(",", var_ref), ")", code_block
    
#Handles function declaration
def fn_let():
    return "let", fn_decl, ZeroOrMore(",", fn_decl)
    
#Handles function call
def fn_call():
    return var_ref, func_parameters

#########################
#Non-Interpretable types#
#########################

#Declares what types can be their own line
def valid_line():
    return [if_statement, print_func, fn_let, fn_decl, fn_call, var_let, var_decl, arithmetic_expression]

#Declares what types can be evaluated to a value
def evaluatable():
    return [if_statement, arithmetic_expression, fn_call, code_block, arithmetic_expression, boolean_expression]
    
def func_parameters():
    return "(", Optional(evaluatable), ZeroOrMore(",", evaluatable), ")"

#######################
#Interpreter Interface#
#######################

#Commenting format to pass into Arpeggio.ParserPython
def comment():
    return RegExMatch('#.*')

#Top level of the grammar
def code():
    return ZeroOrMore(valid_line), EOF
