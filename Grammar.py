from arpeggio import *
from arpeggio import RegExMatch as _

def arithemtic_expression():    return  [(multerm, addop, arithemtic_expression),multerm]
def multerm():                  return [(primary, mulop, multerm),primary]
def primary():                  return [integer, ('(',arithemtic_expression,')')]

def integer(): return _(r'-?\d+')
def addop(): return ["+", "-"]
def mulop(): return ["*","/"]
def relop(): return  ['==','!=','>=','>','<=','<']
