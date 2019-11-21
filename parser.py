#pip install arpeggio
from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython
from arpeggio import PTNodeVisitor
from arpeggio import visit_parse_tree
from arpeggio import Sequence
from arpeggio.export import PMDOTExporter
from arpeggio.export import PTDOTExporter
from AstVisitor import AstVisitor, Binding
from Interpreter import Interpreter
import sys
import string



aToz = []
for i in string.ascii_lowercase:
    aToz.append(i)
identChars = []
nums = ['0','1','2','3','4','5','6','7','8','9']
for i in (string.ascii_letters):
    identChars.append(i)
for i in nums:
    identChars.append(i)
identChars.append("_")
'''begin grammar rules for parser'''

def program(): return               (code, EOF)

def comment(): return               ("#", _(r'.*'))

def code(): return                  ZeroOrMore(statement)

def statement(): return             (ZeroOrMore('\n'), 
                                     [("let", variable_declaration), 
                                        assignment, 
                                        expr], 
                                     ZeroOrMore('\n'))

def variable_declaration(): return  (decl, ZeroOrMore((",", ZeroOrMore('\n'), decl)))

def decl(): return                  (identifier, Optional(("=", expr)))

def identifier(): return            aToz, ZeroOrMore(identChars)

def variable_reference(): return    identifier

def if_expression(): return         (expr, brace_block, Optional(("else", brace_block)))

def assignment(): return            (identifier, "=", expr)

def expr(): return                  [("fn", function_definition), 
                                     ("if", if_expression), 
                                     boolean_expression, 
                                     arithmetic_expression]

def boolean_expression(): return    (arithmetic_expression, relop, arithmetic_expression)

# def arithmetic_expression(): return [(mult_term, addop, arithmetic_expression), 
#                                      mult_term]

def arithmetic_expression(): return (mult_term, ZeroOrMore(addop, mult_term))

# def mult_term(): return             [(primary, mulop, mult_term,), 
#                                      primary]

def mult_term(): return             (primary, ZeroOrMore(mulop, primary))

def primary(): return               [integer, 
                                     function_call, 
                                     variable_reference, 
                                     ("(", arithmetic_expression, ")")]

def integer(): return               (Optional("-"), OneOrMore(nums))

def addop(): return                 ["+", "-"]

def mulop(): return                 ["*", "/"]

def relop(): return                 ["==", "!=", ">=", ">", "<=", "<"]

def function_call(): return         [(variable_reference, "(", call_arguments, ")"), 
                                     ("print", "(", call_arguments, ")")]

def call_arguments(): return        Optional((expr, ZeroOrMore((",", expr))))

def function_definition(): return   (param_list, brace_block)

def param_list(): return            [("(", identifier, ZeroOrMore((",", identifier)), ")"), 
                                     ("(",")")]

def brace_block(): return           (ZeroOrMore('\n'), "{", ZeroOrMore('\n'), code, "}", ZeroOrMore('\n'))


'''-------------------------------------------------------------------------'''
        
        

parser = ParserPython(program, comment, debug=False, ws='\t\r ')   
                              # calc is the root rule of the grammar
                              # Use param debug=True for verbose debugging
                              # messages and grammar and parse tree visualization
                              # using graphviz and dot
                              # add debug=True for thorough print and .dot file
                              # dot -Tpng -O .\program_parse_tree.dot to turn dot to png


#Read input from file
fileName = sys.argv[1]
file = open(fileName, "r")
toEval = ""
for line in file:
    toEval = toEval + str(line)

'''toEval = 
let add_n = fn (n) { fn (x) { x + n }}
let add_2 = add_n(2)
print(add_2(3))
'''
            
'''let x = 1
            let y = 2
            let z = 3
            let yTimex = fn(y, x) {
                print(y*x)
                y = 5
                x = 6
                print(y*x)
                print(z)
            }
            yTimex(y, x)
            print(y)
            print(x)
            yTimex(5, 2)

         ''' 

#Create parse tree
parse_tree = parser.parse(toEval)

#print parse tree as .dot file for viewing
# PTDOTExporter().exportFile(parse_tree, "parse_tree.dot")

#Create AST
ast = visit_parse_tree(parse_tree, AstVisitor(debug=False))

#Execute and store final result into result using interpreter
result = ast.accept(Interpreter(), Binding())