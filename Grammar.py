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
def term():
    return factor, ZeroOrMore(["*", "/"], factor)
    
#One or more terms added/subtracted together
def arithmetic_expression():
    return term, ZeroOrMore(["+", "-"], term)

####################
#Built in Functions#
####################

def print_func():
    return "print(", arithmetic_expression, ")"

#######################
#Interpreter Interface#
#######################

#Commenting format to pass into Arpeggio.ParserPython
def comment():
    return RegExMatch('#.*')

#Top level of the grammar
def code():
    return ZeroOrMore(print_func), EOF