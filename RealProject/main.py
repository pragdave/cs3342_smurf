from arpeggio import *
from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython
from arpeggio.cleanpeg import ParserPEG
from visitorAlg import SmurfVisitor
import os

def program(): return code, EOF
def comment(): return _(r'#.*')
def code() : return ZeroOrMore(statement)
def statement() : return [("let", variable_declaration) , assignment , expr]
def variable_declaration(): return decl, ZeroOrMore(",", decl)
def decl(): return identifier, Optional("=", expr)
def identifier() : return [_(r'[a-z]')], ZeroOrMore([_(r'a-zA-Z_0-9')])
def variable_reference(): return identifier
def if_expression(): return expr, brace_block, Optional( "else", brace_block )
def assignment(): return identifier, "=", expr
def expr(): return [("fn", function_definition), function_call, ("if", if_expression) , boolean_expression ,arithmetic_expression]
def boolean_expression(): return arithmetic_expression, relop, arithmetic_expression
def arithmetic_expression(): return [(mult_term, addop, arithmetic_expression) , mult_term]
def mult_term(): return [(primary, mulop, mult_term) , primary]
def primary():  return [integer, function_call , variable_reference , ( "(", arithmetic_expression, ")")]
def integer(): return _(r'-?[0-9]+')
def integer(): return Optional("-"), _(r'[0-9]+')
def addop(): return ['+',  '-']
def mulop(): return ['*' , '/']
def relop(): return ['==' , '!=' , '>=' , '>' , '<=' , '<']
def function_call(): return [("print", "(", call_arguments, ")"), (variable_reference, "(", call_arguments, ")")]
def call_arguments(): return Optional(expr, ZeroOrMore((",", expr)))
def function_definition(): return param_list, brace_block
def param_list():  return [("(", identifier, ZeroOrMore(",", identifier), ")") ,  ("(",")")]
def brace_block(): return "{", code, "}"

def main(debug = False):
    #current_dir = os.path.dirname(__file__)
    #test_program = open(os.path.join(current_dir, 'C:\\Users\\mailt\Documents\\GitHub\\cs3342_smurf\\test_cases\\00_expr.smu')).read()
    #PictureParser = ParserPEG(main, "program")
    parser = ParserPython(program, comment, debug = debug)
    #parse_tree = parser_parse(test_program)
    #parsing_tree = parser.parse(fileString)

    #parsing_treePic = PictureParser.parse("1")
    file_object = open("mytest.smu", "r")
    fileString = file_object.read()
    parsing_tree = parser.parse(fileString)
    print(f"parsing_tree: {parsing_tree}")
    print(f"typeof tree: {type(parsing_tree)}")
    result = visit_parse_tree(parsing_tree, SmurfVisitor(debug=True))
    binding = {}
    result.eval(binding)
    #print(f"HELLO WORLD")
    print(f"result: {result}")
    print(f"typeof result: {type(result)}")

    #print(f"typeOfName result: {type(result).__name__}")
    #print(f"result: {binding}")
    #print(f"typeof result: {type(binding).__name__}")


if __name__ == "__main__":
    main(debug=True)
