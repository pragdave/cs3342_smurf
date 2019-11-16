from arpeggio import RegExMatch, Optional, ZeroOrMore, OneOrMore, EOF


##############
#Math Portion#
##############

#Int or float or nothing
def number():
    return RegExMatch('\d*\.\d*|\d+')

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
    return RegExMatch('\w+'), "=", arithmetic_expression

#Handles variable declaration
def let():
    return "let", var_decl, ZeroOrMore(",", var_decl)

#Handles boolean expressions ==, !=, >=, >, <=, <
def boolean_expression():
    return arithmetic_expression, ["==", "!=", ">=", ">", "<=", "<"], arithmetic_expression

#Handles a print statement
def print_func():
    return "print(", [boolean_expression, arithmetic_expression], ZeroOrMore(",", [boolean_expression, arithmetic_expression]), ")"

#######################
#Interpreter Interface#
#######################

#Commenting format to pass into Arpeggio.ParserPython
def comment():
    return RegExMatch('#.*')

#Top level of the grammar
def code():
    return ZeroOrMore([print_func, let, var_decl]), EOF