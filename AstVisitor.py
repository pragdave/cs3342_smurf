from arpeggio import PTNodeVisitor
import math

class AstVisitor(PTNodeVisitor):

    def visit_integer(self, node, children):
        printState(node, children, 'integer')
         #print("self:" + str(self))
        if children[0] == "-":            
            val = ''
            for i in range(1, len(children)):
                val = val + str(children[i])
            return Int(val, '-')
        else:
            val = ''
            for i in children:
                val = val + str(i)
            return Int(val)
        
    def visit_primary(self, node, children):
        printState(node, children, 'primary')
         #print("self:" + str(self))
        return children[0]
    
    def visit_mult_term(self, node, children):
        printState(node, children, 'mult_term')
         #print("self:" + str(self))
        return binop_list(children)
    
    def visit_arithmetic_expression(self, node, children):
        printState(node, children, 'arithmetic_expression')
         #print("self:" + str(self))
        return binop_list(children)
    
    def visit_assignment(self, node, children):
        return Assignment(children[0], children[1])
            
    def visit_code(self, node, children):
        return Code(children)
    
    def visit_decl(self, node, children):
        printState(node, children, 'decl')
         #print("self:" + str(self))
        return VarDec(children[0], children[1])
    
    def visit_variable_declaration(self, node, children):
        if len(children) > 1:
            defl = DecList()
            for i in children:
                if i != '\n':
                    defl.push(i)
            return defl
        else:
            return children[0]
        
    def visit_variable_reference(self, node, children):
        printState(node, children, 'var_ref')
         #print("self:" + str(self))
        return VarRef(children)
    
    def visit_boolean_expression(self, node, children):
        return RelOp(children[0], children[1], children[2])
    
    def visit_relop(self, node, children):
        return children[0]
        
    def visit_if_expression(self, node, children):
        printState(node, children, 'if_expr' )
        if len(children) < 3:
            return If(children[0], children[1])
        else:
            return IfElse(children[0], children[1], children[2])
       
    def visit_function_definition(self, node, children):
        printState(node, children, 'func_def')
        return FnDef(children[0], children[1])
    
    def visit_function_call(self, node, children):
        printState(node, children, 'function_call')
         #print("self:" + str(self))
        # print("Calling function " + children[0].getName())
        if children[0].getName() == 'print':
            return Printer(children[1])
        elif len(children) > 1:
            return FnCall(children[0], children[1])
        else:
            return FnCall(children[0], [])
        
    def visit_param_list(self, node, children):
        l = []
        for i in children:
            l.append(i)
        return l
    
    def visit_call_arguments(self, node, children):
        l = []
        for i in children:
            l.append(i)
        return l

    def visit_identifier(self, node, children):
        i = ''
        for l in children:
            i = i + l
        return i

    
class Binding:
    def __init__(self, outer={}):
        self.bindings={}
        self.outer = outer
        
    def push(self):
        return Binding(self)
    
    def pop(self):
        return self.outer
        
    def set_var(self, name, value):
        self.bindings[name] = value
        
    def set_var_val(self, name, value):
        if name in self.bindings:
            self.bindings[name] = value    
        else:
            raise LookupError(name + " not declared in set val")

    def get_var(self, name):
        if name in self.bindings:
            return self.bindings.get(name, 0)
        elif self.outer:
            return self.outer.get_var(name)
        else:
            raise LookupError(name + " not declared in get var")

    def print(self):
        print(str(self.outer))
        print(str(self.bindings))
             
def printState(node, children, funcName):
    pass
    # print("-----------------" + funcName + "-----------------")
    # for i, n in enumerate(node):
    #     print(str(type(n)) + "node[" + str(i) + "]:" + str(n))
    # for i, c in enumerate(children):
    #     print(str(type(c)) + "children[" + str(i) + "]:" + str(c))

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
        self.sign = sign
        self.value = value
        
    def accept(self, visitor, binding):
        return visitor.evaluate_Int(self, binding)
    
    def print(self):
        print("Int value: " + str(self.value))

class binOp:
    def __init__(self, l, op, r):
        self.left = l
        self.op = op
        self.right = r
        
    def accept(self, visitor, binding):
        return visitor.evaluate_binOp(self, binding)
        
    def print(self):
        print("BinOp")
        print("lval: -------------") 
        self.left.print()
        print("op:" + self.op)
        print("rval ----")
        self.right.print()

class RelOp:
    def __init__(self, l, op, r):
        self.left = l
        self.op = op
        self.right = r
        

    def accept(self, visitor, binding):
        return visitor.evaluate_RelOp(self, binding)

class Assignment:
    def __init__(self, name, expression):
        self.name = name
        self.expression = expression
        
    def accept(self, visitor, binding):
        return visitor.evaluate_Assignment(self, binding)

class Code:
    def __init__(self, expressions):
        self.expressions = expressions
        
    def accept(self, visitor, binding):
        return visitor.evaluate_Code(self, binding)

class VarDec:
    def __init__(self, name, value):
        self.name = name
        self.value = value

    def accept(self, visitor, binding):
        return visitor.evaluate_VarDec(self, binding)

class DecList:
    def __init__(self, decls=[]):
        self.decls = decls
        
    def push(self, decl):
        self.decls.append(decl)
        print(str("declarations pushed: " + str(self.decls)))
        
    def accept(self, visitor, binding):
        return visitor.evaluate_DecList(self, binding)

class VarRef:
    def __init__(self, name):
        n = ''
        for l in name:
            n = n + l         
        self.name = n
          
    def accept(self, visitor, binding):
        return visitor.evaluate_VarRef(self, binding)
    
    def getName(self):
        return self.name

class Printer:
    def __init__(self, expressions):
        # print("-------------------------------------got print expr of " + str(expression))
        self.expressions = expressions
  
    def accept(self, visitor, binding):
        return visitor.evaluate_Printer(self, binding)

class If:
    def __init__(self, expr, code):
        self.expr = expr
        self.code = code
                
    def accept(self, visitor, binding):
        return visitor.evaluate_If(self, binding)
        
class IfElse:
    def __init__(self, expr, ifCode, elseCode):
        self.expr = expr
        self.ifCode = ifCode
        self.elseCode = elseCode
          
    def accept(self, visitor, binding):
        return visitor.evaluate_IfElse(self, binding)

class FnDef:
    def __init__(self, params, body):
        # print("params: " + str(params))
        # print("body: " + str(body))
        self.params = params
        self.body = body

    def accept(self, visitor, binding):
        return visitor.evaluate_FnDef(self, binding)
    
class FnCall:
    def __init__(self, name, args):
        self.name = name
        self.args = args
 
    def accept(self, visitor, binding):
        return visitor.evaluate_FnCall(self, binding)
            
class Thunk:
    def __init__(self, params, block, binding):
        self.params = params
        self.block = block
        self.binding = binding
 
    def accept(self, visitor, binding, params):
        return visitor.evaluate_Thunk(self, binding, params)