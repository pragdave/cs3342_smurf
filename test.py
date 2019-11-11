#pip install arpeggio
from arpeggio import Optional, ZeroOrMore, OneOrMore, EOF
from arpeggio import RegExMatch as _
from arpeggio import ParserPython
from arpeggio import PTNodeVisitor
from arpeggio import visit_parse_tree
import string
import math



aToz = []
for i in string.ascii_lowercase:
    aToz.append(i)
identChars = []
for i in (string.ascii_letters + string.digits + "_"):
    identChars.append(i)
nums = ['0','1','2','3','4','5','6','7','8','9']

'''begin grammar rules for parser'''

def program(): return               (code, EOF)

def comment(): return               ("#", _(r'.*'))

def code(): return                  ZeroOrMore(statement)

def statement(): return             [("let", variable_declaration), 
                                     assignment, 
                                     expr,
                                     comment]

def variable_declaration(): return  (decl, ZeroOrMore((",", decl)))

def decl(): return                  (identifier, Optional(("=", expr)))

def identifier(): return            (aToz, ZeroOrMore(identChars))

def variable_reference(): return    identifier

def if_expression(): return         (expr, brace_block, Optional(("else", brace_block)))

def assignment(): return            (identifier, "=", expr)

def expr(): return                  [("fn", function_definition), 
                                     ("if", if_expression), 
                                     boolean_expression, 
                                     arithmetic_expression]

def boolean_expression(): return    (arithmetic_expression, relop, arithmetic_expression)

def arithmetic_expression(): return [(mult_term, addop, arithmetic_expression), 
                                     mult_term]

def mult_term(): return             [(primary, mulop, mult_term,), 
                                     primary]

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

def brace_block(): return           ("{", code, "}")


'''-------------------------------------------------------------------------'''

'''Begin semantic analysis rules'''

class CalcVisitor(PTNodeVisitor):

    def visit_integer(self, node, children):
        print("-----------------integer-----------------")
        print("self:" + str(self))
        for i, n in enumerate(node):
            print(str(type(n)) + "node[" + str(i) + "]:" + str(n))
        for i, c in enumerate(children):
            print(str(type(c)) + "children[" + str(i) + "]:" + str(c))
        if children[0] == "-":            
            val = ''
            for i in children:
                val = val + str(i)
            return Int(val, '-')
        else:
            val = ''
            for i in children:
                val = val + str(i)
            return Int(val)
        
    def visit_primary(self, node, children):
        print("-----------------primary-----------------")
        print("self:" + str(self))
        for i, n in enumerate(node):
            print(str(type(n)) + "node[" + str(i) + "]:" + str(n))
        for i, c in enumerate(children):
            print(str(type(c)) + "children[" + str(i) + "]:" + str(c))
        return children[0]
    
    def visit_mult_term(self, node, children):
        print("-----------------multerm-----------------")
        print("self:" + str(self))
        print("node:" + str(node))
        for i, c in enumerate(children):
            print("children[" + str(i) + "]:" + str(c))
        return binop_list(children)
    
    def visit_arithmetic_expression(self, node, children):
        print("-----------------arithmetic_expr-----------------")
        print("self:" + str(self))
        for i, n in enumerate(node):
            print(str(type(n)) + "node[" + str(i) + "]:" + str(n))
        for i, c in enumerate(children):
            print(str(type(c)) + "children[" + str(i) + "]:" + str(c))
        return binop_list(children)
    
    def visit_assignment(self, node, children):
        return Assignment(children[0], children[1])
            
    def visit_code(self, node, children):
        return Code(children)
    
    def visit_decl(self, node, children):
        print("-----------------decl-----------------")
        print("self:" + str(self))
        for i, n in enumerate(node):
            print(str(type(n)) + "node[" + str(i) + "]:" + str(n))
        for i, c in enumerate(children):
            print(str(type(c)) + "children[" + str(i) + "]:" + str(c))
        return VarDec(children[0], children[1])
    
    def visit_variable_reference(self, node, children):
        print("-----------------variable_reference-----------------")
        print("self:" + str(self))
        for i, n in enumerate(node):
            print(str(type(n)) + "node[" + str(i) + "]:" + str(n))
        for i, c in enumerate(children):
            print(str(type(c)) + "children[" + str(i) + "]:" + str(c))
        return VarRef(children)
    
    def visit_function_call(self, node, children):
        print("-----------------function_call-----------------")
        print("self:" + str(self))
        for i, n in enumerate(node):
            print(str(type(n)) + "node[" + str(i) + "]:" + str(n))
        for i, c in enumerate(children):
            print(str(type(c)) + "children[" + str(i) + "]:" + str(c))
        if children[0].getName() == 'print':
            return Printer(children[1])

def binop_list(nodes):
    left = nodes[0]
    size = len(nodes)
    offset = 1
    while (offset < size):
        op = nodes[offset]
        right = nodes[offset+1]
        left = binOp(left, op, right)
        offset+=2
    return left
          
class Int:
    value = 0
    
    def __init__(self, value, sign='+'):
        print("value = " + str(value))
        self.sign = sign
        self.value = value
        
    def evaluate(self, binding):
        if self.sign == '-':
            return -1*int(self.value, 10)
        else:
            return int(self.value, 10)
    
    def print(self):
        print("Int value: " + str(self.value))

class binOp:
    def __init__(self, l, op, r):
        self.left = l
        self.op = op
        self.right = r
        
    def evaluate(self, binding):
        lval = self.left.evaluate(binding)
        rval = self.right.evaluate(binding)
        if self.op == '+':
            return lval + rval
        elif self.op == '-':
            return lval - rval
        elif self.op == '*':
            return lval * rval
        elif self.op == '/':
            return math.trunc(lval/rval)
        
    def print(self):
        print("BinOp")
        print("lval: -------------") 
        self.left.print()
        print("op:" + self.op)
        print("rval ----")
        self.right.print()

class Assignment:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression
        
    def evaluate(self, binding):
        val = self.expression.evaluate(binding)
        binding.set_var(self.name, val)   
        return val     

class Binding:
    def __init__(self):
        self.bindings={}
        
    def set_var(self, name, value):
        self.bindings[name] = value

    def get_var(self, name):
        return self.bindings.get(name, 0)

    def print(self):
        print(str(self.bindings))

class Code:
    def __init__(self, expressions):
        self.expressions = expressions
        
    def evaluate(self, binding):
        value = ''
        for ex in self.expressions:
            value = ex.evaluate(binding)
        return value

class VarDec:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def evaluate(self, binding):
        val = self.value.evaluate(binding)
        binding.set_var(self.name, val)
        return val
    
class VarRef:
    def __init__(self, name):
        n = ''
        for l in name:
            n = n + l         
        self.name = n
        
    def evaluate(self, binding):
        return binding.get_var(self.name)
    
    def getName(self):
        return self.name

class Printer:
    def __init__(self, expression):
        self.expression = expression
        
    def evaluate(self, binding):
        val = self.expression.evaluate(binding)
        print("Print: " + str(val))
        return val


parser = ParserPython(program, comment, debug=False)   
                              # calc is the root rule of the grammar
                              # Use param debug=True for verbose debugging
                              # messages and grammar and parse tree visualization
                              # using graphviz and dot
                              # add debug=True for thorough print and .dot file
                              # dot -Tpng -O .\program_parse_tree.dot to turn dot to png

# parse_tree = parser.parse('''
#                             let x = 0
#                             if 312 <= 4 { 
#                                 x = 4 
#                                 print(3 + 2)

#                             } 
#                             else {
#                                 x = 5 #a comment
#                                 print(2 + 5)
#                             }
#                             #comment x 
#                             let y = 6
#                           ''')   

toEval = '''print(1 + 2 * 5)'''
parse_tree = parser.parse(toEval)

print("parse_tree:" + str(parse_tree))                         

result = visit_parse_tree(parse_tree, CalcVisitor(debug=True))

print("---------------result----------------")

binding = Binding()
res = result.evaluate(binding)
print(result)
try:
    res.print()
    binding.print()
except:
    binding.print()
    
print(toEval + " = " + str(res))

print("---------------result----------------")

                          