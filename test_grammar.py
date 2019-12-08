from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _

def calc():    return OneOrMore(arithemtic_expression), EOF
def arithemtic_expression(): return multerm, ZeroOrMore(["+", "-"], multerm)
def multerm():       return primary, ZeroOrMore(["*","/"], primary)
def primary(): return [integer, ('(',arithemtic_expression,')')]
def integer(): return _(r'-?[0-9]+')
