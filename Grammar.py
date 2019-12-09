from arpeggio import *
from arpeggio import RegExMatch as _


def expr():                     return [arithmetic_expression],EOF
def arithmetic_expression():    return  [(multerm, addop, arithmetic_expression),multerm]
def multerm():                  return [(primary, mulop, multerm),primary]
def primary():                  return [integer, ('(',arithmetic_expression,')')]

def integer(): return _(r'-?\d+')
def addop(): return ["+", "-"]
def mulop(): return ["*","/"]
def relop(): return  ['==','!=','>=','>','<=','<']
